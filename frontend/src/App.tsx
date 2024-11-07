import { useState } from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Graph from "./components/Graph";
import { Desktop } from "./components/Desktop/Desktop";
import { Button } from "@mui/material";
import SelectForecastSize from "./components/SelectForecastSize";
import { DataSeries } from "./types";
import DropdownFilter from "./components/DropdownFilter";

function App() {
  const [showGraph, setShowGraph] = useState(false);
  const serverURL = import.meta.env.VITE_SERVER_URL;
  const [predictedData, setPredictedData] = useState<DataSeries>();

  // Dropdown Filter
  const [, setSelectedDataType] = useState("");

  const handleSelectChange = (value: string) => {
    setSelectedDataType(value);
  }


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
        <Route 
          path="/graph" 
          element={
            <div>
              
              <DropdownFilter onSelectChange={handleSelectChange} />
              <Graph predictedData={predictedData} />
              <SelectForecastSize setPredictedData={setPredictedData} />
            </div>
          }
        />
         </Routes>

        <Button color="success" size="medium" onClick={handleLoginClick}>
         </Button> 

     </Router>
      
    </>
  );


export default App;

