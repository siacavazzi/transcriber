import React from 'react';
import Button from '../components/Button';

const Home: React.FC = () => {
  const handleClick = () => {
    alert('Button Clicked!'); // this is a place holder, when the button is clicked it should begin to record
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-6">Welcome to Transcriber Beta! press the button to begin recording your meeting </h1>
        <Button 
          onClick={()=>handleClick()}>Record!
        </Button>
      </div>

      {/*prompt and recording box*/}
      <div className="container mx-auto text-center">
        <input
          type="text"
          className="border p-2 mt-4"
          placeholder="Type something..."
        />
      </div>
    </div>
  );
};

export default Home;




