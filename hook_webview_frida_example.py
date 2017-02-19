import frida
import sys

package_name = "com.jni.anto.kalip"


def get_messages_from_js(message, data):
            print(message)
            print (message['payload'])
 

def instrument_load_url():

        hook_code = """
        setTimeout(function(){
        Dalvik.perform(function () {

            var WebView = Dalvik.use("android.webkit.WebView");

            WebView.loadUrl.overload("java.lang.String").implementation = function (s) {

                send(s.toString());

                this.loadUrl.overload("java.lang.String").call(this, s);

            };

        });

    },0);
        """

        return hook_code

process = frida.get_device_manager().enumerate_devices()[-1].attach(package_name)
script = process.create_script(instrument_load_url())
script.on('message',get_messages_from_js)
script.load()
sys.stdin.read()
              
