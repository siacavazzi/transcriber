import React from 'react'

interface ButtonProps {
    onClick?: () => void;
    children: React.ReactNode;
    className?: string;
}

const Button: React.FC<ButtonProps> = ({ onClick, children, className = '' }) => {
    return (
      <button
        className={`bg-blue-500 text-white font-bold py-2 px-4 rounded ${className}`}
        onClick={onClick}
      >
        {children}
      </button>
    );
  };
  
  export default Button;