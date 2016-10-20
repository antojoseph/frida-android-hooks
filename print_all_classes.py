import frida
import sys

package_name = "com.example.android"


def get_messages_from_js(message, data):
            print (message)
 

def instrument_debugger_checks():
    hook_code = """setTimeout(function(){Java.enumerateLoadedClasses({onMatch: function(className) {send(className);},onComplete:function(){send("done");}});},0);"""
    return hook_code

process = frida.get_device_manager().enumerate_devices()[-1].attach(package_name)
script = process.create_script(instrument_debugger_checks())
script.on('message',get_messages_from_js)
script.load()
sys.stdin.read()
