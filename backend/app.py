import eventlet
eventlet.monkey_patch()
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask import Flask, request, jsonify, session
from extensions import socketio
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource 


from lib.room import Room
from flask_cors import CORS
from lib.models import db, User
from flask_bcrypt import Bcrypt
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
bcrypt = Bcrypt(app)
api = Api(app)
migrate = Migrate(app, db)
socketio.init_app(app)
connected_clients = {}
CORS(app, supports_credentials=True,resources={r"/*": {"origins": "http://localhost:3000"}})


def get_room(sid):
    try:
        return connected_clients[sid]
    except:
        print("Error: No room found")
        return None



@app.get('/room')
def make_room_code():
    code = Room.generate_code(connected_clients)
    connected_clients[code] = Room()
    return {'room_code': code}

@app.get('/ping')
def ping():
    return jsonify({'ping':'server online'})

@app.post('/audio')
def handle_audio():
    try:
     # this is for testing - proper error handling will be implemented
        file = request.files['audio_data']
        room_code = request.form.get('room_code')
        room = get_room(room_code)

        text = room.get_transcript(file)
        return jsonify({'transcript': text})

    except Exception as e:
        print('error')
        print(e)
        return {'error': "error"}, 500

def current_user():
    user = User.query.filter(User.id == session.get('user_id')).first()
    return user

@app.get('/check_session')
def check_session():
    user = current_user()
    if user:
        return jsonify(user.secure_dict()), 200
    else:
        return {'message':'No user found'}, 400


@app.post('/login')
def login():
    try:
        json = request.json
        user = User.query.filter(User.email == json["email"]).first()
            
        if user and bcrypt.check_password_hash(user.pass_hash, json["password"]):
            session["user_id"] = user.id
            print(session.get('user_id'))
            return user.secure_dict(), 202
        else:
            return {"error":"Incorrect login information. Please try again."}
    except Exception as e:
        return {"error":str(e)}
    
@app.get('/logout')
def logout():
    try:
        session.pop('user_id', None)
        return {}, 202
    except:
        return {"error":"User could not be logged out."}, 500




# RESTful api for user accounts
class Users(Resource):
    def post(self):
        try:
            json = request.json
        # check if the email is already in the db
            user_with_same_email = User.query.filter(User.email == json['email']).first()
            print(user_with_same_email)
            if user_with_same_email:
                return {"error":"Email already in use. Please try a different email."}
        
            pw_hash = bcrypt.generate_password_hash(json['password']).decode('utf-8')
            new_user = User(email = json['email'], pass_hash=pw_hash, fname=json['fname'], lname=json['lname'], creation_date=date.today())
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id

            return new_user.secure_dict(), 201
        except Exception as e:
            return { 'error': str(e)}, 500
        
    def get(self):
        try:
            json = request.json
            user = User.query.filter(User.email == json["email"]).first()
            
            if user and bcrypt.check_password_hash(user.pass_hash, json["password"]):
                return user.to_dict(), 202
            else:
                return {"error":"Incorrect email or password."}
        except Exception as e:
            return {"error":str(e)}
        
    def delete(self):
        try:
            json = request.json
            user = User.query.filter(User.email == json["email"]).first()

            if not user:
                return {"error":"user does not exist"}
            db.session.delete(user)
            db.session.commit()
            return {"message": "user deleted"}, 200

        except Exception as e:
            return { 'error': str(e)}, 500
            
api.add_resource(Users, '/users')
        
if __name__ == '__main__':
    print("Server Started...")
    socketio.run(app, host='0.0.0.0', port=5000)