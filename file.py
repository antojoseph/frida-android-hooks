import frida
import sys
from subprocess import Popen

package_name = "com.jni.anto.kalip"


def get_messages_from_js(message, data):
        print(message)



            
 

def fake_file_checks():
        hook_code = """
        setTimeout(function(){
        Dalvik.perform(function () {

            var TM = Dalvik.use("java.io.File");

            TM.exists.implementation = function () {
                send("Called - canRead()");
                console.log(this.path['value']);
                var file_path = this.path['value'];
                var root_locations = ['/bin/su','/xbin/su','Superuser.apk','busybox','/sdcard/test'];
                for (i = 0; i < root_locations.length; i++) {
                        console.log(" Comparing " + root_locations[i] + " with "+file_path);

                        if(root_locations[i] === file_path){
                            console.log('lalal');
                            return false;
                        }
                }
            return true;
            };

        });

    },0);
        """

        return hook_code
Popen("adb forward tcp:27042 tcp:27042", shell=True).wait()
process = frida.get_device_manager().enumerate_devices()[-1].attach(package_name)
script = process.create_script(fake_file_checks())
script.on('message',get_messages_from_js)
script.load()
sys.stdin.read()

