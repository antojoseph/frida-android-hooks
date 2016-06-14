import frida
import sys

package_name = "com.jni.anto.kalip"


def get_messages_from_js(message, data):
            print(message)
            print (message['payload'])
 

def instrument_debugger_checks():

        hook_code = """
        setTimeout(function(){
        Java.perform(function () {

            var TM = Java.use("android.os.Debug");

            TM.isDebuggerConnected.implementation = function () {

                send("Called - isDebuggerConnected()");

            return false;
            };

            var TMS = Java.use("android.telephony.TelephonyManager");
            TMS.getDeviceId.implementation = function () {
                send("Called - deviceID()");
                return "pwn3d";
            };

        });

    },0);
        """

        return hook_code


process = frida.get_usb_device().attach(package_name)
script = process.create_script(instrument_debugger_checks())
script.on('message',get_messages_from_js)
script.load()
sys.stdin.read()
