import './HomePage.css';
import {Autocomplete, Button, TextField, InputAdornment, IconButton, Typography} from '@mui/material'
import {Padding, PlaceOutlined, Visibility, VisibilityOff} from '@mui/icons-material'
import React, {useState} from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

function HomePage() {
    const [ song, setSongValue ] = useState('');
    // const [songList, setSongListValue] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const [songs, setSongs] = useState([]);
    const [recs,setRecs] = useState([]);
    const [imgs, setImgs] = useState([]);
    const url = "https://bettermusicrecommender.onrender.com";

    const handleClick = (e) => {
        //e.preventDefault();
        if (song.trim() !== "" && song.includes(" by ")) {
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

    const handleRecs = (e) =>{
        if(songs.length < 1){
            alert("You did not add any songs");
        }
        else{
                setIsLoading(true); // Set loading to true
              //  alert('isLoading set to true:', isLoading); // Debug: Check state value *after* setting
                try {
                            axios.post(url + `/getRecs`, {songs})
                        .then((response) => {
                            
                            setRecs(response.data[0]);
                            setImgs(response.data[1]);
                        })
                } catch (err) {
                setError(err); // Set error if something goes wrong
                } finally {
                setIsLoading(false); // Set loading to false regardless of success or failure
                //alert('isLoading set to false:', isLoading); // Debug: Check state value *after* setting
                }
          
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
                    <li key={index} >{song}<br></br> <br></br> </li>
                ))}
                </ul>
           )}
            

             <div>
          
                        <Button
                                     onClick={handleRecs}
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
            <div>
                <p>needs to be in format: Song by Artist with spaces before and after the word by</p>
            </div>

            {isLoading && <p>Loading...</p>}
            {recs.length > 0 && (
                <ul className="mt-4">
                {recs.map((rec, index) => (
                    <li key={index} ><img src={imgs[index]} /><br></br> <br></br>{rec}<br></br> <br></br></li>
                ))}
                </ul>
           )}
        </div>
        
       
    );
  }
  
  
  export default HomePage;