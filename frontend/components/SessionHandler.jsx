import { useEffect } from 'react';
import { useUser } from './UserContext';

const SessionHandler = ({ children }) => {
    const { updateUser } = useUser();

    const OPTIONS = {
        method: "GET",
        credentials: 'include'
    }

    useEffect(() => {
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
    }, []);

    return <>{children}</>;
};
export default SessionHandler;
