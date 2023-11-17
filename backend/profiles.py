### Profiles database structure ###

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

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


profiles = Flask (__name__)
profiles.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
db.SQLAlchemy(profiles)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forst_name = db.Column()

