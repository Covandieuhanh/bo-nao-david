#!/usr/bin/env python3
"""Cài các điểm ghi nhật ký vào cấu hình Claude Code hoặc Codex đã được David chọn."""
import argparse
import json
import os
from pathlib import Path
import shlex
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ghi


def install(app, config, store=None, only_if_installed=False):
    script = Path(ghi.__file__).resolve()
    settings = json.loads(config.read_text(encoding="utf-8")) if config.exists() else {}
    hooks = settings.get("hooks", {})
    start = hooks.get("SessionStart", [])
    if only_if_installed and not any(
        "/tu-dong-hoa/dong-bo.sh" in item.get("command", "")
        and str(ghi.REPO) in item.get("command", "")
        for group in start for item in group.get("hooks", [])
    ):
        return False
    command = [sys.executable, "-I", str(script), "hook", app]
    if store is not None:
        selected = store.expanduser().resolve()
        os.environ["DAVID_NHAT_KY_DIR"] = str(selected)
        ghi.store_root()
        command = ["env", f"DAVID_NHAT_KY_DIR={selected}", *command]
    command_text = shlex.join(command)
    marker = f"/nhat-ky/ghi.py hook {app}"
    updated = False
    for event in ghi.HOOKS[app]:
        groups = hooks.setdefault(event, [])
        matches = [h for g in groups for h in g.get("hooks", [])
                   if marker in h.get("command", "").replace("'", "").replace('"', "")]
        if not matches:
            groups.append({"hooks": [{"type": "command", "command": command_text, "timeout": 30}]})
            updated = True
        elif not only_if_installed:
            for item in matches:
                if item["command"] != command_text:
                    item["command"] = command_text
                    updated = True
    if not updated:
        return False
    settings["hooks"] = hooks
    config.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=config.parent, delete=False) as file:
        temporary = Path(file.name)
        try:
            json.dump(settings, file, ensure_ascii=False, indent=2)
            file.write("\n")
            file.flush()
            os.replace(temporary, config)
        finally:
            temporary.unlink(missing_ok=True)
    return True


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("ung_dung", choices=ghi.HOOKS)
    cli.add_argument("--cau-hinh", type=Path)
    cli.add_argument("--kho", type=Path)
    cli.add_argument("--da-cai-bo-nao", action="store_true")
    options = cli.parse_args()
    if options.ung_dung == "claude-code":
        home = Path(os.environ.get("CLAUDE_CONFIG_DIR", str(Path.home() / ".claude")))
        default = home / "settings.json"
    else:
        home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
        default = home / "hooks.json"
    if install(options.ung_dung, options.cau_hinh or default, options.kho, options.da_cai_bo_nao):
        print(f"Đã cài điểm ghi nhật ký cho {options.ung_dung}.")


if __name__ == "__main__":
    main()
