import "../App.css";
import "./MainPage.css";
import { useEffect, useState } from "react";
import Slider, { DEFAULT_SLIDER_VAL } from "./Slider";
// import RadioButtons from "./RadioButtons";
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
  const [filterGender, setFilterGender] = useState<string>("NoFilter");
  const [filterRace, setFilterRace] = useState<string>("NoFilter");

  // Data State Variables
  const [pastData, setPastData] = useState<DataSeries>();
  const [pastDataUnbiased, setPastDataUnbiased] = useState<DataSeries>();
  const [predictedData, setPredictedData] = useState<DataSeries>();
  const [predictedDataUnbiased, setPredictedDataUnbiased] =
    useState<DataSeries>();

  async function getPastData() {
    const formattedData = await getPastDataAPICall([filterGender, filterRace]);

    if (formattedData) {
      setPastData({
        name: "Known Data",
        color: "#2933f2", 
        data: formattedData,
      });
    }
  }
  async function getPastDataUnbiased() {
    const formattedData = await getPastDataUnbiasedAPICall([filterGender, filterRace]);

    if (formattedData) {
      setPastDataUnbiased({
        name: "Known Data (Unbiased)",
        color: "#f72525", //red
        data: formattedData,
      });
    }
  }
  async function predictData() {
    const formattedData = await predictDataAPICall([filterGender, filterRace], sliderValue);

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
      sliderValue
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
  }, []);

  const navigate = useNavigate();

  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

   return (
    <div style={{ textAlign: "center", marginTop: "20px", padding: "20px"}}  aria-live="polite">
      {/* Page Title */}
      <div className="fixed-bar">
      <h1 
      style={{ fontSize: "2rem", color: "#2d2d2d", marginBottom: "20px" }}
      aria-labelledby="dashboard"
      id="dashboard"
    >
      Dashboard
    </h1>
    {/* Menu Button */}
      <Box
        sx={{
          position: "absolute",
          top: 0,
          right: 0,
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

      
      <div className="main-container">
        {/* Graph Component */}
        <Graph
          pastData={pastData}
          pastDataUnbiased={pastDataUnbiased}
          predictedData={predictedData}
          predictedDataUnbiased={predictedDataUnbiased}
        />
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
        <PredictButton onClick={updatePrediction} aria-label="Update prediction"/>
        <br />
        <br />
        <ExportGraphButton aria-label="Export graph"/>
      </div>
    </div>
  );
}
export default MainPage;
