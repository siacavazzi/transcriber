import React from 'react';
import Button from '../components/Button';

const Home: React.FC = () => {
  const handleClick = () => {
    alert('Button Clicked!');
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-6">Welcome to Tailwind CSS with TypeScript</h1>
        <Button 
          onClick={handleClick}>Click me!
        </Button>
      </div>
    </div>
  );
};

export default Home;




