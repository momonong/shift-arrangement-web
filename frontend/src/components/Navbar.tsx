import React, { useState } from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import { Link } from 'react-router-dom';

function Navbar() {
  const [anchorEls, setAnchorEls] = useState<{ [key: string]: HTMLElement | null }>({});

  const handleClick = (buttonId: string) => (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEls({ ...anchorEls, [buttonId]: event.currentTarget });
  };  

  const handleClose = (buttonId: string) => () => {
    setAnchorEls({ ...anchorEls, [buttonId]: null });
  };

  // 假設有五個按鈕，每個按鈕有不同的菜單項目
  const buttons = [
    { id: 'btn_shift', 
      label: '排班選項', 
      menuItems: [{ label: '個人班表上傳', 
                    link: '/personal-schedule-upload' }, 
                  { label: '檢視所有班表', 
                    link: '/view-all-schedules' },
                  { label: '檢核排班後班表',
                    link: '/verify-schedule'}] },
    { id: 'btn_2', 
    label: '按鈕2', 
    menuItems: [{ label: '功能2-1', 
                  link: '/func2-1' }, 
                { label: '功能2-2', 
                  link: '/func2-2' }] },
    { id: 'btn_3', 
    label: '按鈕3', 
    menuItems: [{ label: '功能3-1', 
                  link: '/func3-1' }, 
                { label: '功能3-2', 
                  link: '/func3-2' }] },
  ];

  return (
    <AppBar position="fixed" style={{ width: '100%' }}>
      <Toolbar disableGutters>
        <img 
          src="https://static.wixstatic.com/media/37c673_8d76871adc8c49e181f4f9119139acb1~mv2.png/v1/fill/w_120,h_104,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/pic-10.png" 
          alt="Laboratory for Artificial Intelligence and Multiscale Modeling" 
          style={{ marginLeft: '25px', marginRight: '4px', height: '25px', width: 'auto' }} 
        />
        <Typography
          variant="h6"
          noWrap
          sx={{
            mr: 2,
            display: { xs: 'none', md: 'flex' },
            fontFamily: 'monospace',
            fontWeight: 700,
            letterSpacing: '.075rem',
            color: 'inherit',
            textDecoration: 'none',
          }}
        >
          LAiMM
        </Typography>
        <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
          {buttons.map((button) => (
            <React.Fragment key={button.id}>
              <Button
                style={{ margin: '5px', textTransform: 'none', color: 'white' }}
                onClick={handleClick(button.id)}
              >
                {button.label}
              </Button>
              <Menu
                id={`menu-${button.id}`}
                anchorEl={anchorEls[button.id]}
                open={Boolean(anchorEls[button.id])}
                onClose={handleClose(button.id)}
              >
                {button.menuItems.map((menuItem, index) => (
                  <MenuItem key={index} onClick={handleClose(button.id)} component={Link} to={menuItem.link}>
                    {menuItem.label}
                  </MenuItem>
                ))}
              </Menu>
            </React.Fragment>
          ))}
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
