import eventlet
eventlet.monkey_patch()
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask import Flask, request, jsonify
from extensions import socketio
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource 
from lib.key import key
from deepgram import Deepgram
import asyncio
import threading
from lib.room import Room
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
migrate = Migrate(app, db)
socketio.init_app(app)
connected_clients = {}
CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


def get_room(sid):
    try:
        return connected_clients[sid]
    except:
        print("Error: No room found")



@app.get('/room')
def make_room_code():
    code = Room.generate_code(connected_clients)
    connected_clients[code] = Room()
    return {'room_code': code}



@app.post('/audio')
def handle_audio():
    #try:
    if True: # this is for testing - proper error handling will be implemented
        file = request.files['audio_data']
        room_code = request.form.get('room_code')
        room = get_room(room_code)

        text = room.get_transcript(file)
        return jsonify({'transcript': text})

    #except Exception as e:
        print('error')
        print(e)
        return {'error': "error"}



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)