import eventlet
eventlet.monkey_patch()
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask import Flask, request, jsonify
from extensions import socketio

from lib.key import key
from deepgram import Deepgram
import asyncio
import threading
from lib.room import Room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio.init_app(app)
connected_clients = {}

def get_room(sid):
    try:
        return connected_clients[sid]
    except:
        print("Error: No room found")


@socketio.on('connect')
def handle_connect():
    room = Room(request.sid)
    connected_clients[request.sid] = room
    print('Client connected: '+ request.sid)


@socketio.on('audio-chunk')
def handle_audio_chunk(data):
    print('got audio! '+ request.sid)
    room = get_room(request.sid)
    file = room.record(data)
    print(file)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)