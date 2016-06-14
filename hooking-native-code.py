import frida
import sys

package_name = "com.jni.anto.kalip"


def get_messages_from_js(message, data):
            print(message)
            print (message['payload'])
 

def instrument_debugger_checks():

        hook_code = """
       Interceptor.attach (Module.findExportByName ( "libc.so", "read"), {
            onEnter: function (args) {
            send (Memory.readUtf8String (args [1]));     
        },
            onLeave: function (retval) {
    }
});"""
    return hook_code


process = frida.get_usb_device().attach(package_name)
script = process.create_script(instrument_debugger_checks())
script.on('message',get_messages_from_js)
script.load()
sys.stdin.read()
