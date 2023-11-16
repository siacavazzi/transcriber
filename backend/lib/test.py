 # Example filename: deepgram_test.py

from deepgram import Deepgram
import asyncio
import aiohttp
from key import key

# Your Deepgram API Key
class Deepgram():
  def __init__(self):
    self.DEEPGRAM_API_KEY = key

# URL for the realtime streaming audio you would like to transcribe
  URL = 'http://stream.live.vc.bbcmedia.co.uk/bbc_world_service'

  async def main(self):
  # Initialize the Deepgram SDK
    deepgram = Deepgram(self.DEEPGRAM_API_KEY)

  # Create a websocket connection to Deepgram
  # In this example, punctuation is turned on, interim results are turned off, and language is set to UK English.
    try:
      deepgramLive = await deepgram.transcription.live({
      'smart_format': True,
      'interim_results': False,
      'diarize':True,
      'language': 'en-US',
      'model': 'nova-2',
    })
    except Exception as e:
      print(f'Could not open socket: {e}')
      return

  # Listen for the connection to close
    deepgramLive.register_handler(deepgramLive.event.CLOSE, lambda c: print(f'Connection closed with code {c}.'))

    def output(data):
      if(data):
        print(data)
        speaker = data['channel']['alternatives'][0]['words'][0]['speaker']
        print("==============")
      

 
        print(f"Speaker: {speaker} Text: {data['channel']['alternatives'][0]['transcript']}")

  # Listen for any transcripts received from Deepgram and write them to the console
    deepgramLive.register_handler(deepgramLive.event.TRANSCRIPT_RECEIVED, output)

  # Listen for the connection to open and send streaming audio from the URL to Deepgram
    async with aiohttp.ClientSession() as session:
      async with session.get(URL) as audio:
        while True:
          data = await audio.content.readany()
          deepgramLive.send(data)

        # If no data is being sent from the live stream, then break out of the loop.
          if not data:
              break

  # Indicate that we've finished sending data by sending the customary zero-byte message to the Deepgram streaming endpoint, and wait until we get back the final summary metadata object
    await deepgramLive.finish()

# If running in a Jupyter notebook, Jupyter is already running an event loop, so run main with this line instead:
#await main()
  asyncio.run(main())