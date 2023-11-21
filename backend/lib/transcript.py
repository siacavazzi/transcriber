from fuzzywuzzy import fuzz, process

class Transcript():
    
    def __init__(self, target_length=10):
        self.transript = ''
        self.target_length = target_length
        self.seconds = 0


    def add_chunk(self, chunk):
        
        print(f"chunk: {chunk}, transcript: {self.transript}")
        self.transript = self.transript + " " + chunk
        print("TRANSCRIPT COMPLETE +++++++")
        print(self.transript)
        # self.seconds += 1
        # if self.seconds < 6:
        #     print(chunk)
        #     return 
        # # check if transcript is long - if it is then trim the last few words, use combine_strings, then append
        

    def get_partial_ts(self, sub_chunk):
        partial_ts = self.transript
        if len(partial_ts) == 0: # if the transcript is empty
            partial_ts = sub_chunk
        elif len(partial_ts.split(' ')) > 10000: # if the transcript has more than 10 words -> this is purely for optimization
            pass # THIS IS JUST A PLACEHOLDER FOR NOW
        else: # any other case
            print("COMBINING STRINGS...")
            partial_ts = self.combine_strings(partial_ts, sub_chunk)
        return partial_ts


    
    def combine_strings(self, s1, s2):
    # Find the best partial match of s2 in s1
        match = process.extractOne(s2, [s1], scorer=fuzz.partial_ratio)

    # Check if a match was found
        if match:
            match_string, ratio = match  # Unpacking the match string and ratio
            print("ratio:", ratio)
        
        # Ensure ratio is a numerical value for comparison
            ratio = float(ratio)  # Convert ratio to float for comparison

            if ratio > 60:  # Threshold for minimum similarity
                overlap_start = s1.find(match_string)
                overlap_len = len(match_string)
                overlap_end = overlap_start + len(match_string)

            # Remove the overlapping part from the second string and concatenate
                return s1 + s2[overlap_len:]
            else:
            # If no significant match, just concatenate the strings
                return s1 + " " + s2

    # If no match at all
        return s1 + " " + s2


        
