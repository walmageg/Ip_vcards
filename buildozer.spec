[app]

# (str) Title of your application
title = {َVQR

# (str) Package name
package.name = VQR

# (str) Package domain (unique domain for your app, e.g. org.test)
package.domain = org.mycompany

# (str) Source code where the main.py live
source.dir = .

# (str) Main .py file
source.main = main.py

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# هنا بتحط المكتبات اللي محتاجها زي: python3,kivy,requests
requirements = python3,kivy

# (str) Application entry point
entrypoint = main.py

# (str) Supported orientation (one of: landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png


[buildozer]

# (int) Target Android API (most recent stable API)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android application theme, built from styles.xml
# (one of "fullscreen", "standard", "light", "black", "dark", "material")
android.theme = @android:style/Theme.Material.Light

# (list) Permissions
# مثال: android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.permissions = INTERNET

# (str) Android arch (armeabi-v7a, arm64-v8a, x86, x86_64)
android.arch = arm64-v8a

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = True

# (bool) Indicate whether to include source code in apk
copy_source = False

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (list) Supported orientations
orientation = portrait

# (list) List of service classes to include
#android.services =

# (str) Additional arguments for gradle
# android.gradle_arguments = -Xmx4g

# (bool) Enable android logcat (true/false)
log_level = 2
logcat_filter = *:S python:D

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True
