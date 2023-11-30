import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';
import Link from 'next/link';
import { useUser } from './UserContext'
import { useRouter } from 'next/router';

const pages = ['My Transcripts'];
const settings = ['Logout'];

function ResponsiveAppBar() {
  const { user, updateUser } = useUser();
  const router = useRouter();

  function handleLogout() {
    const OPTIONS = {
      method: "GET", 
      credentials: 'include',
    headers: {
      "Accept": "application/json",
        "Content-Type": "application/json"
    },
  }

    fetch("http://localhost:5000/logout", OPTIONS)
      .then(resp => {
        if (resp.ok) {
          updateUser(null);
        }
      })

  }

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Transcriber Beta
          </Typography>
          {user ?
            <div>
              <Typography variant="h6" component="div" >
                Welcome, {user.fname}
              </Typography>
              <Button onClick={() => handleLogout()} color="inherit">Logout</Button>
            </div>
            : <Button onClick={()=> router.push('/login')}color="inherit">Login</Button>}
        </Toolbar>
      </AppBar>
    </Box>
  );
}
export default ResponsiveAppBar;