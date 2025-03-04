import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
import HomePage from "./HomePage/HomePage";
// import SignUpPage from "./SignUpPage/SignUpPage";
// import TravelPlanPage from "./TravelPlanPage/TravelPlanPage";
// import MapPage from "./MapPage/MapPage";




function App() {
  return (
    <Router>
      <Routes>
          <Route path="/" element={<HomePage/>} />
        
      </Routes>
    </Router>
  );
}


export default App;