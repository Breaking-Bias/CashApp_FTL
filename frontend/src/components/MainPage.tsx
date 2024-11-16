import "../App.css";
import "./MainPage.css";
import { useEffect, useState } from "react";
import Slider, { DEFAULT_SLIDER_VAL } from "./Slider";
import RadioButtons from "./RadioButtons";
import GenderDropdownFilter from "./GenderDropdownFilter";
import RaceDropdownFilter from "./RaceDropdownFilter";
import PredictButton from "./PredictButton";
import Graph from "./Graph";
import {
  getPastDataAPICall,
  getPastDataUnbiasedAPICall,
  predictDataAPICall,
  predictDataUnbiasedAPICall,
} from "../ApiCalls";
import { DataSeries } from "../types";
import ExportGraphButton from "./ExportGraphButton";
import { Button, Menu, MenuItem, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { IconButton, Tooltip } from '@mui/material';
import HelpIcon from '@mui/icons-material/Help';


function MainPage() {
  // Component State Variables
  const [sliderValue, setSliderValue] = useState<number>(DEFAULT_SLIDER_VAL);
  const [mode, setMode] = useState<string>("0");
  const [filterGender, setFilterGender] = useState<string>("NoFilter");
  const [filterRace, setFilterRace] = useState<string>("NoFilter");

  // Data State Variables
  const [pastData, setPastData] = useState<DataSeries>();
  const [pastDataUnbiased, setPastDataUnbiased] = useState<DataSeries>();
  const [predictedData, setPredictedData] = useState<DataSeries>();
  const [predictedDataUnbiased, setPredictedDataUnbiased] =
    useState<DataSeries>();

  async function getPastData() {
    const formattedData = await getPastDataAPICall([filterGender, filterRace], mode);

    if (formattedData) {
      setPastData({
        name: "Known Data",
        color: "#2933f2", 
        data: formattedData,
      });
    }
  }
  async function getPastDataUnbiased() {
    const formattedData = await getPastDataUnbiasedAPICall([filterGender, filterRace], mode);

    if (formattedData) {
      setPastDataUnbiased({
        name: "Known Data (Unbiased)",
        color: "#f72525", //red
        data: formattedData,
      });
    }
  }
  async function predictData() {
    const formattedData = await predictDataAPICall([filterGender, filterRace], sliderValue, mode);

    if (formattedData) {
      setPredictedData({
        name: "Predicted Data",
        color: "#030985", // dark blue
        data: formattedData,
      });
    }
  }
  async function predictDataUnbiased() {
    const formattedData = await predictDataUnbiasedAPICall(
      [filterGender, filterRace],
      sliderValue,
      mode
    );

    if (formattedData) {
      setPredictedDataUnbiased({
        name: "Predicted Data (Unbiased)",
        color: "#750101", // dark red
        data: formattedData,
      });
    }
  }

  function updatePrediction() {
    getPastData();
    getPastDataUnbiased();
    predictData();
    predictDataUnbiased();
  }
  

  useEffect(() => {
    getPastData();
  }, [mode]);

  const navigate = useNavigate();

  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

   return (
    <div style={{ textAlign: "center", marginTop: "50px", padding: "10px 20px"}}  aria-live="polite">
      {/* Page Title */}
      <div className="fixed-bar" style={{ backgroundColor: "white", padding: "20px", position: "fixed", width: "100%", top: 0, left: 0, zIndex: 100 }}>
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'flex-start', width: '100%' }}>
      <h1 
      style={{ fontSize: "2rem", color: "#2d2d2d", marginBottom: "10px" }}
      aria-labelledby="dashboard"
      id="dashboard"
    >
      Dashboard
    </h1>

      <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginTop: "0px" }}>
          <h3 style={{ fontSize: "1rem"}}>I want data on </h3>
          <RadioButtons
            mode={mode}
            setMode={setMode}
          />
      </div>
    </div>

      {/* Menu Button */}
      <Box
        sx={{
          position: "absolute",
          top: 0,
          right: 100,
          padding: 2,
        }}
      >
        <Button variant="contained" color="success" onClick={handleClick}
          aria-haspopup="true"
          aria-expanded={Boolean(anchorEl)}
          aria-controls="menu"
          aria-label="Open menu">
          Menu
        </Button>
        <Menu anchorEl={anchorEl} open={Boolean(anchorEl)} onClose={handleClose} aria-label="Main menu">
          <MenuItem onClick={() => navigate("/guidance")}>How To Use</MenuItem>
        </Menu>
      </Box>
      
      </div>
    
      <div style={{ display: "flex", height: "100vh" }}>
          <div style={{
            width: "80%", 
            padding: "20px", 
            borderRight: "1px solid #ccc",
            display: "flex",
            justifyContent: "center",
            alignItems: "center"
            }}>
            
      <div className="main-container">
        {/* Graph Component */}
        <div style={{marginTop: "200px" }}>
          <Graph
            pastData={pastData}
            pastDataUnbiased={pastDataUnbiased}
            predictedData={predictedData}
            predictedDataUnbiased={predictedDataUnbiased}
          />
        </div>
        <br />

        {/* Prediction Size Section */}
        <Box display="flex" alignItems="center" justifyContent="center">
          <h3 style={{ marginRight: "8px" }}>Prediction size:</h3>
          <Tooltip title="The slider is used to adjust the prediction size. Longer timeframe when slider is on the right.">
            <IconButton aria-label="Help with prediction size slider" style={{ padding: "4px", marginLeft: "4px" }}>
              <HelpIcon />
            </IconButton>
          </Tooltip>
        </Box>

        <Slider sliderValue={sliderValue} setSliderValue={setSliderValue} aria-labelledby="prediction-size-label"/>
        <br />

        {/* Filter Section */}
        <h3>Filter:</h3>
        <Box display="flex" alignItems="center" justifyContent="space-between" gap={2} flexWrap="wrap" width="100%">
        <GenderDropdownFilter
          // filterFactor={filterFactor}
          // setFilterFactor={setFilterFactor}
          aria-label="Gender filter options"
          onSelectChange={(value: string) => setFilterGender(value)
          }
        />
        <RaceDropdownFilter
          aria-label="Race filter options"
          onSelectChange={(value: string) => setFilterRace(value)}
        />
        
        </Box>
        <Box display="flex" alignItems="center" justifyContent="center">
        < PredictButton onClick={updatePrediction} aria-label="Update prediction"/>
        <Tooltip title="Choose Prediction Size and Filter first, then click on this button to visualize.">
            <IconButton aria-label="Make forecast button" style={{ padding: "4px", marginLeft: "4px" }}>
              <HelpIcon />
            </IconButton>
          </Tooltip>
        </Box>
        <br />
        <br />
        <ExportGraphButton aria-label="Export graph"/>
      </div>
    </div>

     {/* Right Section for Revenue Data */}
    <div style={{ flex: 1,  textAlign: "right", marginLeft: "200px", marginTop: "200px"}}>
      <h2 style={{ fontSize: "1.5rem", color: "#2d2d2d", marginBottom: "20px" }}>Revenue Loss</h2>
    {/* Graph for Revenue Data */}
      <p>Loading revenue data...</p>
    </div>
  </div>
  </div>
  );
}
export default MainPage;
