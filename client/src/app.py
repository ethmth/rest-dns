import socketio
import requests
from python_hosts import Hosts, HostsEntry

API_URL = "http://localhost:5000"

hosts = Hosts(path='hosts.txt')

r = requests.get(url = f"{API_URL}/ips")

def get_hosts():
    print("get_hosts called")
    for ip in r.json():
        try:
            if (hosts.exists(names=[f"{ip['id']}.remote"])):
                hosts.remove_all_matching(name=f"{ip['id']}.remote")
            entry = HostsEntry(entry_type='ipv4', address=f"{ip['ip']}", names=[f"{ip['id']}.remote"])
            hosts.add([entry])
            hosts.write()
        except:
            pass
        try:
            if (hosts.exists(names=[f"{ip['id']}.localnet"])):
                hosts.remove_all_matching(name=f"{ip['id']}.localnet")
            entry = HostsEntry(entry_type='ipv4', address=f"{ip['local']}", names=[f"{ip['id']}.localnet"])
            hosts.add([entry])
            hosts.write()
        except:
            pass

get_hosts()
sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server")
    get_hosts()


    return

@sio.event
def ip_posted(data):
    #print("ip_posted", data)
    get_hosts()
    return

sio.connect(API_URL)
sio.wait()
