import io from 'socket.io-client';
import { useEffect, useState } from 'react';

const options = { mimeType: 'audio/webm' };

function downloadBlob(blob: Blob, baseFilename = 'audiofile') {
  // Create a timestamp
  const timestamp = new Date().toISOString().replace(/[\-:T]/g, '').slice(0, 14);

  // Construct a unique filename using the baseFilename and timestamp
  const filename = `${baseFilename}_${timestamp}.webm`;

  // Create an object URL for the blob
  const url = window.URL.createObjectURL(blob);

  // Create a new anchor element
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;

  // Append the anchor to the document body and trigger the download
  document.body.appendChild(a);
  a.click();

  // Clean up by removing the anchor and revoking the object URL
  document.body.removeChild(a);
  window.URL.revokeObjectURL(url);
}
const AudioStreamer = () => {
  const [roomCode, setRoomCode] = useState(null);
  const [isRecording, setIsRecording] = useState(false)
  const [transcript, setTranscript] = useState('')



  function sendAudio(roomCode: any, data: Blob) {
    console.log(data)

    const formData = new FormData();
    formData.append('room_code', roomCode);
    formData.append('audio_data', data);

    const OPTIONS = {
      method: "POST",
      body: formData
    }
    fetch("http://localhost:5000/audio", OPTIONS)
    .then(resp => resp.json())
    .then(data => setTranscript(data['transcript']))
  }

  useEffect(() => {
    let mediaRecorder: any;
    const startRecording = () => {
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
          const mediaRecorder = new MediaRecorder(stream, options);
          console.log(mediaRecorder.mimeType)
          mediaRecorder.ondataavailable = e => {
            if (e.data.size > 0 && roomCode) {
              //socket.emit('audio-chunk', e.data);
              console.log("sending audio... Room: " + roomCode)
              sendAudio(roomCode, e.data)
              // downloadBlob(e.data)
              /// maybe change this to be a post....
            }
          };

          mediaRecorder.start(1000); // chunk size in ms -> change this as desired
        })
        .catch(err => console.error('Audio capture error:', err));
    }

    const stopRecording = () => {
      if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop()
      }
    };

    if (isRecording) {
      startRecording()
    } else {
      stopRecording()
    }
  }, [isRecording, roomCode]);

  function getRoomCode() {
    fetch("http://localhost:5000/room")
      .then(resp => resp.json())
      .then(data => setRoomCode(data['room_code']))
    setIsRecording(true)
  }




  return (
    <div>
      <button onClick={getRoomCode}>Start Recording</button>
      <p>{transcript}</p>
    </div>
  )

};

export default AudioStreamer;