import "../App.css";
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
        color: "#2933f2", //blue
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
    <div>
      {/* Menu button at the top */}
      <Box display="flex" justifyContent="flex-start" padding={2}>
        <Button variant="contained" color="primary" onClick={handleClick}>
          Menu
        </Button>
        <Menu
          anchorEl={anchorEl}
          open={Boolean(anchorEl)}
          onClose={handleClose}
        >
          <MenuItem onClick={() => navigate("/guidance")}>How To Use</MenuItem>
        </Menu>
      </Box>

      {/* Main content */}
      <Graph
        pastData={pastData}
        pastDataUnbiased={pastDataUnbiased}
        predictedData={predictedData}
        predictedDataUnbiased={predictedDataUnbiased}
      />
      <br />
      <h3>Prediction size:</h3>
      <Slider sliderValue={sliderValue} setSliderValue={setSliderValue} />
      <br />
      <h3>Filter:</h3>
      <GenderDropdownFilter
        // filterFactor={filterFactor}
        // setFilterFactor={setFilterFactor}
        onSelectChange={(value: string) => setFilterGender(value)
        }
      />
      <RaceDropdownFilter
        onSelectChange={(value: string) => setFilterRace(value)}
      />
      <PredictButton onClick={updatePrediction} />
      <br />
      <br />
      <ExportGraphButton />
    </div>
  );
}

export default MainPage;
