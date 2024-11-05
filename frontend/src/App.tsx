import { useState } from "react";
import "./App.css";
import {BrowserRouter as Router, Routes, Route, useNavigate} from "react-router-dom";
import Graph from "./components/Graph";
import { Desktop } from "./components/Desktop/Desktop";
import { Button } from "@mui/material";
import SelectForecastSize from "./components/SelectForecastSize";
import { DataSeries } from "./types";

function App() {
  const [showGraph, setShowGraph] = useState(false);
  const serverURL = import.meta.env.VITE_SERVER_URL;

  const [predictedData, setPredictedData] = useState<DataSeries>();

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
        <Route path="/graph" element={<Graph predictedData={predictedData} />} />
      </Routes>

      <SelectForecastSize setPredictedData={setPredictedData} />
     </Router>
      {/* <Desktop />
      <Button color="success" size="medium" onClick={handleLoginClick}>
        Login
      </Button> */}

      
    </>
  );
}

export default App;
