import io from 'socket.io-client';
import { useEffect, useState } from 'react';

const options = { mimeType: 'audio/webm' };

// NOTE: add chunk length as a prop 
const AudioStreamer = () => {
  const [roomCode, setRoomCode] = useState(null);
  const [isRecording, setIsRecording] = useState(false)
  const [transcript, setTranscript] = useState('')

  // function to post audio to backend
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
              console.log("sending audio... Room: " + roomCode)
              sendAudio(roomCode, e.data)
              // downloadBlob(e.data) <- debug method, uncomment to download blobs to browser
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
    } // useeffect triggers when these vars change
  }, [isRecording, roomCode]);

  // get a room code when starting (to handle multiple users)
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