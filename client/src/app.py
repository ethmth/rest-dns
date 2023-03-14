import socketio
import requests
from python_hosts import Hosts, HostsEntry
import os
import signal
import sys

API_URL = "http://127.0.0.1:24601"
if "API_URL" in os.environ:
	API_URL = os.environ['API_URL']

HOSTS_PATH="hosts"
if "HOSTS_PATH" in os.environ:
	HOSTS_PATH = os.environ['HOSTS_PATH']

PORTS_PATH="ports"


HOSTS_OG="hosts_og"
HOSTS_TEMP="hosts_temp"

os.system(f'cp {HOSTS_PATH} {HOSTS_OG}')


class GracefulKiller:
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        os.system(f'cat {HOSTS_OG} > {HOSTS_PATH}')
        print("Gracefully exiting")
        os.killpg(0, signal.SIGKILL)
        quit()

def get_hosts():
    try: 
        r = requests.get(url = f"{API_URL}/ips")
        with open(HOSTS_TEMP, 'w') as file:
            file.write("")
        hosts = Hosts(path=HOSTS_TEMP)
        os.system(f'printf "" > {PORTS_PATH}')
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

            try:
                if ip['port'] != "none" and ip['port'] != "Invalid":
                    os.system(f"echo '{ip['port']} {ip['id']}' >> {PORTS_PATH}")
            except:
                pass
        os.system(f'cat {HOSTS_OG} {HOSTS_TEMP} > {HOSTS_PATH}')

    except:
        pass

get_hosts()
sio = socketio.Client()

@sio.event
def connect():
    get_hosts()
    return

@sio.event
def ip_posted(data):
    get_hosts()
    return

if __name__ == '__main__':
    killer = GracefulKiller()
    sio.connect(API_URL)
    sio.wait()
