import tempfile
from openai import OpenAI
import asyncio
import random
import string
from .key import key
import mimetypes
from werkzeug.utils import secure_filename


class Room():

    @classmethod
    def generate_code(cls, room_codes,length=4):
        room_code = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
        while room_code in room_codes:
            room_code = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
        return room_code
    
    @classmethod
    def get_mime_type(cls, file_storage):
        print("filename")
        print(file_storage.filename)
        return mimetypes.guess_type(file_storage.filename)[0]
    
    @classmethod
    def get_file_extension(cls, file_storage):
        filename = secure_filename(file_storage.filename)
        return filename.rsplit('.', 1)[1].lower() if '.' in filename else None
    
    def __init__(self):
        
        self.activeFile = None
        self.client = OpenAI()
        self.client.api_key = key

    def get_transcript(self, data):
        print(data)
        file_path = self.record(data)
        text = self.transcribe(file_path)
        return text


    def record(self, data):
        data.seek(0)
        if self.activeFile is None:
            self.activeFile = tempfile.NamedTemporaryFile(delete=False, suffix=".webm", mode='wb')
        self.activeFile.write(data.read())
        #self.activeFile.close()
        return self.activeFile.name

        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm", mode='wb') as temp_file:
            temp_file.write(data.read())  # Write the binary data to the temp file
            temp_file.flush()
            temp_file_path = temp_file.name
            print(temp_file_path)
            return temp_file_path
        
    def transcribe(self, file_path):
        audio_file = open(file_path, "rb")
        transcript = self.client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
            )
        print(transcript)
        return transcript.text
        


