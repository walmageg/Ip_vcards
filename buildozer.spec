[app]

# اسم الباكدج بتاعك
title = VQR
package.name = VQR
package.domain = org.test

# سكربت البداية
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# ملف البايثون الرئيسي
main.py = main.py

# نسخة التطبيق
version = 0.1

# الايقونة
icon.filename = %(source.dir)s/data/icon.png

# Kivy requirements
requirements = python3,kivy

# ممكن تضيف مكتبات تانية هنا
# requirements = python3,kivy,requests

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1

# نسخة API و SDK
android.api = 34
android.sdk = 34

# نسخة NDK
android.ndk = 25b

# build tools ثابتة
android.build_tools = 34.0.0

# منع استخدام نسخ قديمة
p4a.branch = master
android.accept_sdk_license = True



