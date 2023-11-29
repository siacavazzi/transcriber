import { useEffect } from 'react';
import { useUser } from './UserContext';

const SessionHandler = ({ children }) => {
    const { updateUser } = useUser();

    useEffect(() => {
        console.log("Checking session...");
        fetch("/check_session")
            .then(resp => {
                if (resp.ok) {
                    console.log("Check session found user.");
                    resp.json().then(user => updateUser(user));
                } else {
                    console.log(`Check session failed to find user. Status code ${resp.status}`);
                }
            });
    }, [updateUser]);

    return <>{children}</>;
};
export default SessionHandler;
