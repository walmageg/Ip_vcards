[app]
title = QVR
package.name = QVR
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Android specific
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

# Permissions (لو عايز تضيف)
android.permissions = INTERNET

# Entry point
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
