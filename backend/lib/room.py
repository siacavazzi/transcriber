import tempfile

class Room():
    def __init__(self, sid):
        self.uid = sid
        self.activeFile = None

    def record(self, data):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm", mode='wb') as temp_wav:
            temp_wav.write(data)
            return temp_wav.name
