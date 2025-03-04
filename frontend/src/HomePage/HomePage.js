import './HomePage.css';
import {Autocomplete, Button, TextField, InputAdornment, IconButton, Typography} from '@mui/material'
import {Padding, PlaceOutlined, Visibility, VisibilityOff} from '@mui/icons-material'
import React, {useState} from 'react';
import { Link, useNavigate } from 'react-router-dom';

function MapPage() {
    return (
        <div className="page-content-mapper">
            <h1><b>Map</b></h1>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>


           
            <br></br>
            <br></br>
            <br></br>
             <div>
          
                        <Button
                                    // onClick={handleLoginClick}
                                     variant = 'outlined'
                                     label = 'see path'
                                     style = {{
                                         justifyContent: 'center',
                                         alignItems: 'center',
                                         margin: '10px',
                                       
                                         color: 'black'
                                      }}
                            >Back</Button>
            
             </div>
            
        </div>
        
       
    );
  }
  
  
  export default MapPage;