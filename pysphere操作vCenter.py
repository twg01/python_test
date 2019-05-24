#python2.7
from pysphere import VIServer
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

server = VIServer()
server.connect("192.168.90.201","administrator@vsphere.local","1qaz@WSX")

vm1 = server.get_vm_by_name("test")
print(vm1.get_status())