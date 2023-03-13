import socketio
import requests
from python_hosts import Hosts, HostsEntry

API_URL = "http://localhost:5000"

hosts = Hosts(path='hosts.txt')

r = requests.get(url = f"{API_URL}/ips")

for ip in r.json():
    try:
        entry = HostsEntry(entry_type='ipv4', address=f"{ip['ip']}", names=[f"{ip['id']}.remote"])
        hosts.add([entry])
        hosts.write()
        print(ip)
    except:
        pass


exit

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server")
    return

@sio.event
def ip_posted(data):
    print(data)
    return

sio.connect(API_URL)
sio.wait()
