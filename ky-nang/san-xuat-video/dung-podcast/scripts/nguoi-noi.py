#!/usr/bin/env python3
"""Giữ lệnh cũ cho thiết bị đã cài. Tên chuẩn: tach-luot-nguoi-noi.py."""
import os
from pathlib import Path
import sys

script = Path(__file__).resolve().with_name("tach-luot-nguoi-noi.py")
python_options = ["-I"] if sys.flags.isolated else []
os.execv(sys.executable, [sys.executable, *python_options, str(script), *sys.argv[1:]])
