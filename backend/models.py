from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
#from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# Models here ....

class Line(db.Model):
    __tablename__ = "lines"

    id = db.Column(db.Integer, primary_key = True)
    time_ms = db.Column(db.Integer)
    text = db.Column(db.String)

   # transcript_id = 

# Line model - represents one 10s chunk of transcript
# id, transcript_id,start_time, end_time, time_ms?


# Image model - represents images generated for the transcript
# id, transcript_id, time_ms?, image blob data, prompt?

# Transcript model
# attributes: id, user_id, time_started, time_ended, title, description

class Transcript(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    

# GPT comment model - each row is a GPT comment about the transcript
# attributes: id, transcript_id, time_ms, line_id?, text

# Config model - transcription configs
# id, user_id, prompt, generate_images (bool), ... other settings idk yet


# User model
# id, username/ email, name, p/w hash, date created



# associated with user: transcripts, configs

# associated with transcripts: lines, images, comments