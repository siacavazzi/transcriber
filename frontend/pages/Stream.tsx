import io from 'socket.io-client';
import { useEffect } from 'react';

const socket = io('http://localhost:5000');

const AudioStreamer = () => {
    useEffect(() => {
      navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
          const mediaRecorder = new MediaRecorder(stream);
  
          mediaRecorder.ondataavailable = e => {
            if (e.data.size > 0) {
              socket.emit('audio-chunk', e.data);
            }
          };
  
          mediaRecorder.start(1000); // Adjust chunk size as needed
  
          return () => {
            mediaRecorder.stop();
          };
        })
        .catch(err => console.error('Audio capture error:', err));
    }, []);
  
    return <div>Streaming Audio...</div>;
  };
  
  export default AudioStreamer;