import socketio


API_URL = "http://localhost:5000"

sio = socketio.Client()

#@sio.on('connection') 
#def on_connection(data):
@sio.event
def connect():
    print("I connected")
    #print(data)

    return

sio.connect('http://localhost:5000')
sio.wait()