
import React from 'react';
import Button from '../components/Button';
import AudioStreamer from './Stream';

const Home: React.FC = () => {
  const handleClick = () => {
    alert('Button Clicked!');                                   // this is a place holder, when the button is clicked it should begin to record
  };

  const handleClickLeft = () => {
    alert('Left Button Clicked!');
  };

  const handleClickRight = () => {
    alert('Right Button Clicked!');
  };

  return (
                                                    
    <div className="flex items-center justify-center h-screen"> {/*header*/}
      <AudioStreamer/> {/* FOR TESTING*/}
      {/* Toolbar at the top */}
      <div className="flex justify-between w-full p-4 bg-gray-200">
        {/* Left button */}
        <Button onClick={handleClickLeft}>Options</Button>

        {/* Right button */}
        <Button onClick={handleClickRight}>Profile</Button>
      </div>

      <div className="text-center">
        <h1 className="text-4xl font-bold mb-6">Welcome to Transcriber Beta! press the button to begin recording your meeting HI </h1>
      </div>

      <div className="container mx-auto text-center">           {/*prompt and recording box*/}

        <h3
          className="border p-2 mt-4">
          Enter Prompt Here to optimize recording: 
          
          <input                                                  
            type="text"
            className="border p-2"
            placeholder= "Not functioning..."
          />
        </h3>

        <Button                                                 // call the back end funtion to start recording 
          onClick={()=>handleClick()}>Record! 
        </Button>
      </div>

      {/*text box that will contain transcript from backend*/}
      <div className="fixed bottom-0 left-0 right-0 bg-gray-100 p-4 min-h-screen"> 
        <input
          type="text"
          className="border p-2"
          placeholder= "transcript loading..."
        />
      </div>
    </div>
  );
};

export default Home;





