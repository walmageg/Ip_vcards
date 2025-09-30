[app]
title = QVR
package.name = qvr
package.domain = org.qvr
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
# Android SDK / NDK settings
android.api = 34
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
bootstrap = sdl2
android.accept_sdk_license = True

# Permissions (لو محتاج صلاحيات زودها هنا)
android.permissions = INTERNET

[app:source]
# ملفات إضافية عايز تنسخها جوه الـ APK
source.include_patterns = assets/*

[app:package]
package.version = 1
package.numeric_version = 1

[app:icon]
# أيقونة مخصصة (اختياري)
icon.filename = %(source.dir)s/icon.png
