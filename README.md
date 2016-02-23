# webview-hook-frida
Lets you hook LoadURL Method Calls in Frida ( Android )


Setup :

1 . Load Firda -server into your android device . 

$ curl -O https://build.frida.re/frida/android/arm/bin/frida-server
$ adb push frida-server /data/local/tmp/
$ adb shell "chmod 755 /data/local/tmp/frida-server"
$ adb shell "/data/local/tmp/frida-server &" 

2 . Install frida on your machine , easy_install frida

3 . Change the package_name variable in the script to match the application you are instrumenting .

4 . Run python hook_webview_frida_example.py

5 . Run any app which uses Webview loadURL method .

Have fun !
