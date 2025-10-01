[app]
# اسم التطبيق اللي هيظهر للمستخدم
title = Ip Vcards

# الباكدج نيم (مهم يكون فريد)
package.name = ipvcards
package.domain = org.walmageg

# ملفات المشروع
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# إصدار التطبيق
version = 0.1

# المكتبات المطلوبة
requirements = python3,kivy

# الاتجاه
orientation = portrait
fullscreen = 0

# أيقونة التطبيق (اختياري)
# لو عندك أيقونة، حطها في مجلد المشروع واكتب اسمها هنا
# icon.filename = %(source.dir)s/icon.png

# شاشة البداية (اختياري)
# android.presplash = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1

# Android API
android.api = 34
android.minapi = 21

# Build tools
android.build_tools = 34.0.0

# NDK version
android.ndk = 25b

# المعماريات (دعم أجهزة قديمة وحديثة)
android.arch = armeabi-v7a, arm64-v8a

# قبول رخص الـ SDK تلقائياً
android.accept_sdk_license = True
