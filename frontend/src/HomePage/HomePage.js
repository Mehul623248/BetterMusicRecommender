import './HomePage.css';
import {Autocomplete, Button, TextField, InputAdornment, IconButton, Typography} from '@mui/material'
import {Padding, PlaceOutlined, Visibility, VisibilityOff} from '@mui/icons-material'
import React, {useState} from 'react';
import { Link, useNavigate } from 'react-router-dom';

function HomePage() {
    const [ song, setSongValue ] = useState('');
    const handleClick = () => {
        if(song === ''){
            console.log('Song container cannot be empty!');
        }
        else{
            alert(song);
        }
    }
    return (
        <div className="page-content-home">
            <h1><b>Song Recommendations</b></h1>
             <div>
             <TextField
                      label='song'
                      onChange={(e) => setSongValue(e.target.value)}
                      variant='outlined'
                      style = {{backgroundColor: 'grey', borderColor: 'red'}}
                  />
             </div>
             <div>
             <Button
                        onClick={handleClick}
                        variant = 'outlined'
                        label = 'Go'
                        style = {{
                            justifyContent: 'center',
                            alignItems: 'center',
                            margin: '10px',
                            width: '100px',
                            height: '30px',
                            color: 'red'
                        }}
                    >Go</Button>
             </div>
            

             <div>
          
                        <Button
                                    // onClick={handleLoginClick}
                                     variant = 'outlined'
                                     label = 'see path'
                                     style = {{
                                         justifyContent: 'center',
                                         alignItems: 'center',
                                         margin: '10px',
                                       
                                         color: 'red'
                                      }}
                            >Get Recs</Button>
            
             </div>
            
        </div>
        
       
    );
  }
  
  
  export default HomePage;