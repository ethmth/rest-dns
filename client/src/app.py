import socketio

API_URL = "http://localhost:5000"
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