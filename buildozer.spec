[app]
title = VQR Decoder
package.name = vqrdecoder
package.domain = org.vqr
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,sounddevice,numpy,scipy
orientation = portrait
fullscreen = 0

# الأيقونة (ممكن تعدلها لو عندك أيقونة مخصصة)
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

# Android specific
[app.android]
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = armeabi-v7a,arm64-v8a
android.permissions = RECORD_AUDIO,INTERNET
