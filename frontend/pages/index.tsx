import React from 'react';
import Button from '../components/Button';

const Home: React.FC = () => {
  const handleClick = () => {
    alert('Button Clicked!');                                   // this is a place holder, when the button is clicked it should begin to record
  };

  return (
                                                    
    <div className="flex items-center justify-center h-screen"> {/*header*/}
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-6">Welcome to Transcriber Beta! press the button to begin recording your meeting </h1>
      </div>

      <div className="container mx-auto text-center">           {/*prompt and recording box*/}

        <h3
          className="border p-2 mt-4">
          Enter Prompt Here to optimize recording: 
          <input 
                                                           
          type="text"
          className="border p-2"
          placeholder="Type something..."
          />
        </h3>

        <Button                                                 // call the back end funtion to start recording 
          onClick={()=>handleClick()}>Record! 
        </Button>
      </div>

      <div className="fixed bottom-0 left-0 right-0 bg-gray-100 p-4 min-h-screen"> 
        This is a gray box at the bottom of the screen.
      </div>
    </div>
  );
};

export default Home;




