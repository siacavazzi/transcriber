import io from 'socket.io-client';
import { useEffect } from 'react';

const socket = io('http://localhost:5000');
const options = { mimeType: 'audio/webm' };
const AudioStreamer = () => {
    useEffect(() => {
      navigator.mediaDevices.getUserMedia({ audio: true})
        .then(stream => {
          const mediaRecorder = new MediaRecorder(stream, options);
          console.log(mediaRecorder.mimeType)
          mediaRecorder.ondataavailable = e => {
            if (e.data.size > 0) {
              socket.emit('audio-chunk', e.data);
            }
          };
  
          mediaRecorder.start(5000); // chunk size in ms -> change this as desired
  
          return () => {
            mediaRecorder.stop();
          };
        })
        .catch(err => console.error('Audio capture error:', err));
    }, []);
  
    return <div>Streaming Audio...</div>;
  };
  
  export default AudioStreamer;