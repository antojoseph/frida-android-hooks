# frida-android-hooks

Lets you hook LoadURL Method Calls in Frida ( Android )

Welcome to Firda- Hooks ( Android )

You will find different different modules to hook various api calls in the android platform to conduct security analysis. Right now , we have the following modules :

WebView loadUrl() : android.webkit.WebView calls to webview is logged .

getDeviceId() : android.telephony.TelephonyManager detects if the above api is called and can return a fake device id if needed.

isDebuggerConnected() : android.os.Debug checks if a debugger is connected (JDB) to the app instance , can log and re-implement the method to fake it to the application which is being instrumented.

.exists() : java.io.File checks for the presence of files in disk , can log and even hide the presence of files from applications using this api.

Root Bypass Re- Implementation : root.py example on how a method could be re-implemented overriding the root-checks of an android application .

Setup :

1 . Load Firda -server into your android device . 

      $ curl -O https://build.frida.re/frida/android/arm/bin/frida-server

      $ adb push frida-server /data/local/tmp/

      $ adb shell "chmod 755 /data/local/tmp/frida-server"

      $ adb shell "/data/local/tmp/frida-server &" 

2 . Install frida on your machine , easy_install frida

3 . Change the package_name variable in the script to match the application you are instrumenting .

4 . Run python hook_webview_frida_example.py

5 . Run any app which uses the instumented  method / api.

Have fun !



Authors and Contributors

@antojoseph

Support or Contact

Having trouble with Scripts ? Check out our documentation or contact support or Log an Issue and we’ll help you sort it out.
