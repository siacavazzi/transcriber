import { useEffect, useState } from 'react';
import { useUser } from './UserContext';
import Alert from '@mui/material/Alert';

const SessionHandler = ({ children }) => {
    const { updateUser } = useUser();
    const [error, setError] = useState(null)

    const OPTIONS = {
        method: "GET",
        credentials: 'include'
    }

    useEffect(() => {
        try {
            console.log("Checking session...");
            fetch("http://localhost:5000/check_session", OPTIONS)
                .then(resp => {
                    if (resp.ok) {
                        console.log("Check session found user.");
                        resp.json().then(user => updateUser(user));
                    } else {
                        console.log(`Check session failed to find user. Status code ${resp.status}`);
                    }
                });

        } catch (error) {
            setError(error)
        }}
    , []);

return (<>
{error ? <Alert>error</Alert>:<></>}
{children}
</>);
};
export default SessionHandler;
