from fuzzywuzzy import fuzz
class Transcript():
    
    def __init__(self):
        self.transript = ''
        self.last_chunk = None


    def new_chunk(self, chunk):
        if self.last_chunk is None:
            pass

        

        self.last_chunk = chunk
