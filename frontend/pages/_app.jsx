// pages/_app.js
import React from 'react';
import App from 'next/app';
import Header from '../components/Header.jsx';
import {useState, useEffect} from 'react';


// pages/_app.js

const MyApp = ({ Component, pageProps }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    console.log("Checking session...");
    fetch("/check_session")
      .then(resp => {
        if (resp.ok) {
          console.log("Check session found user.");
          resp.json().then(user => setUser(user));
        } else {
          console.log(`Check session failed to find user. Status code ${resp.status}`);
        }
      });
  }, []);

  return (
    <div>
      <Header user={user}/>
      <Component {...pageProps} />
    </div>
  );
};

export default MyApp;

