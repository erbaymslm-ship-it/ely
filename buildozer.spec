[app]
title = ELIXIR TECHNOLOGY
package.name = elixir
package.domain = com.elixir.technology
source.dir = src
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1
requirements = python3,kivy==2.3.0,numpy,pillow,pyjnius
icon.filename = %(source.dir)s/assets/elixir_logo.png
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION
android.gradle_dependencies = com.google.android.gms:play-services-location:21.0.1
android.features = android.hardware.bluetooth
android.accept_sdk_license = True
