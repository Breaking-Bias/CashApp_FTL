import "./App.css";
import {BrowserRouter as Router, Routes, Route, useNavigate} from "react-router-dom";
import { useState } from "react";
import Graph from "./components/Graph";
import { Desktop } from "./components/Desktop/Desktop";
import { Button } from "@mui/material";

function App() {
  const [showGraph, setShowGraph] = useState(false);
  const serverURL = import.meta.env.VITE_SERVER_URL;

  async function makeTestGetRequest() {
    const endpoint = serverURL + "/getinfo";

    try {
      // make the request
      const response = await fetch(endpoint);

      // catch errors in fetch response
      if (!response.ok) {
        throw new Error("Error in response:" + response.statusText);
      }

      // convert the data to json
      const data = await response.json();

      console.log(data);
    } catch (error) {
      console.error("Error:", error);
    }
  }
  function handleLoginClick() {
    setShowGraph(true);
    console.log("Login clicked, showGraph set to:", showGraph); // Log state update
    makeTestGetRequest(); 
  }
  
  return (
    <>
      <Router>
      <Routes>
        <Route path="/" element={<Desktop />} />
        <Route path="/graph" element={<Graph />} />
      </Routes>
    </Router>
      {/* <Desktop />
      <Button color="success" size="medium" onClick={handleLoginClick}>
        Login
      </Button>

      <h1>This is our front end</h1>

      {showGraph && <Graph />} Render Graph conditionally */}
    </>
  );
}

export default App;
