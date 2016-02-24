import frida
import sys

package_name = "com.jni.anto.kalip"


def get_messages_from_js(message, data):
            print(message)
            print (message['payload'])
 

def instrument_root_checks():

        hook_code = """
        setTimeout(function(){
        Dalvik.perform(function () {

            var TM = Dalvik.use("com.jni.anto.kalip.MainActivity");

            TM.isPhoneRooted.implementation = function () {

                send("Called - isPhoneRooted()");

                return false;

            };

        });

    },0);
        """

        return hook_code

process = frida.get_device_manager().enumerate_devices()[-1].attach(package_name)
script = process.create_script(instrument_root_checks())
script.on('message',get_messages_from_js)
script.load()
sys.stdin.read()
              