#!/bin/bash
set -e
cd "$(dirname "$0")"
APP=~/Applications/"Mở Tài Liệu.app"
rm -rf "$APP"; mkdir -p "$APP/Contents/MacOS"
swiftc -O -parse-as-library main.swift trinh-chieu.swift ban-in-va-sua.swift -o "$APP/Contents/MacOS/MoTaiLieu"
cat > "$APP/Contents/Info.plist" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
<key>CFBundleName</key><string>Mở Tài Liệu</string>
<key>CFBundleDisplayName</key><string>Mở Tài Liệu</string>
<key>CFBundleIdentifier</key><string>local.david.motailieu</string>
<key>CFBundleExecutable</key><string>MoTaiLieu</string>
<key>CFBundlePackageType</key><string>APPL</string>
<key>CFBundleShortVersionString</key><string>1.0</string>
<key>LSMinimumSystemVersion</key><string>14.0</string>
<key>NSHighResolutionCapable</key><true/>
<key>CFBundleDocumentTypes</key><array><dict>
<key>CFBundleTypeName</key><string>Tài liệu</string>
<key>CFBundleTypeRole</key><string>Editor</string>
<key>LSHandlerRank</key><string>Alternate</string>
<key>LSItemContentTypes</key><array><string>public.content</string><string>public.data</string></array>
</dict></array>
</dict></plist>
PL
codesign --force -s - "$APP"
echo "OK: $APP"
