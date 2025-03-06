import './HomePage.css';
import {Autocomplete, Button, TextField, InputAdornment, IconButton, Typography} from '@mui/material'
import {Padding, PlaceOutlined, Visibility, VisibilityOff} from '@mui/icons-material'
import React, {useState} from 'react';
import { Link, useNavigate } from 'react-router-dom';

function HomePage() {
    const [ song, setSongValue ] = useState('');
    // const [songList, setSongListValue] = useState([]);

    const [songs, setSongs] = useState([]);
 

    const handleClick = (e) => {
        //e.preventDefault();
        if (song.trim() !== "") {
            setSongs([...songs, song]);
            setSongValue(""); // Clear input field after submission
        }
    }
    const handleClick2 = (e) =>{
        if (songs.length > 0) {
            songs.pop();
            setSongs([...songs])
            //setSongValue(""); // Clear input field after submission
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
                            borderColor: 'red',
                            color: 'red'
                        }}
                    >Go</Button>
                    <Button
                        onClick={handleClick2}
                        variant = 'outlined'
                        label = 'Go'
                        style = {{
                            justifyContent: 'center',
                            alignItems: 'center',
                            margin: '10px',
                            width: '100px',
                            height: '30px',
                            borderColor: 'red',
                            color: 'red'
                        }}
                    >Remove</Button>
             </div>
             
             {songs.length > 0 && (
                <ul className="mt-4">
                {songs.map((song, index) => (
                    <li key={index} >{song}</li>
                ))}
                </ul>
           )}
            

             <div>
          
                        <Button
                                    // onClick={handleLoginClick}
                                     variant = 'outlined'
                                     label = 'see path'
                                     style = {{
                                         justifyContent: 'center',
                                         alignItems: 'center',
                                         margin: '10px',
                                         borderColor: 'red',

                                         color: 'red'
                                      }}
                            >Get Recs</Button>
            
             </div>
            
        </div>
        
       
    );
  }
  
  
  export default HomePage;