// Script taken from : https://github.com/brompwnie/uitkyk


var objectsToLookFor = ["java.net.Socket", "dalvik.system.DexClassLoader", "java.net.URLConnection", "java.net.URL", "java.security.cert.X509Certificate"];
for (var i in objectsToLookFor) {
	Java.perform(function () {
		Java.choose(objectsToLookFor[i], {
			"onMatch": function (instance) {
				if (objectsToLookFor[i] == "java.net.URL" && instance.getProtocol() != "file") {
					console.log("\n[+] Process has Instantiated instance of: " + objectsToLookFor[i]);
					console.log("[*] Process is communicating via " + instance.getProtocol());
					console.log("[+] Communication Details: " + instance.toString());
				}
				if (objectsToLookFor[i] == "dalvik.system.DexClassLoader") {
					console.log("\n[+] Process has Instantiated instance of: " + objectsToLookFor[i]);
					console.log("[*] Process is making use of DexClassLoader");
					console.log("[+] Loader Details: " + instance.toString());
				}
				if (objectsToLookFor[i] == "java.net.Socket") {
					console.log("\n[+] Process has Instantiated instance of: " + objectsToLookFor[i]);
					console.log("[*] Process is making use of a Socket Connection");
					console.log("[+] Socket Details: " + instance.toString());
				}
				if (objectsToLookFor[i] == "java.net.URLConnection") {
					console.log("\n[+] Process has Instantiated instance of: " + objectsToLookFor[i]);
					console.log("[*] Process is making use of a URL Connection");
					console.log("[+] Details: " + instance.toString());
				}
				if (objectsToLookFor[i] == "java.security.cert.X509Certificate") {
					console.log("\n[+] Process has Instantiated instance of: " + objectsToLookFor[i]);
					console.log("[*] Process is making use of a X509Certificate");
					console.log("[+] X509Certificate Details: " + instance.toString());
				}
			},
			"onComplete": function () {
			}
		});
	});
}
