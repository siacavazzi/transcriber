import eventlet
eventlet.monkey_patch()
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask import Flask, request, jsonify
from extensions import socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio.init_app(app)
connected_clients = {}



@socketio.on('audio-chunk')
def handle_stream(data):
    print(data)

@socketio.on('connection')
def handle_connection():
    print("user connected")




if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)