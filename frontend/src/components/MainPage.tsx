import "../App.css";
import { useEffect, useState } from "react";
import Slider, { DEFAULT_SLIDER_VAL } from "./Slider";
import RadioButtons from "./RadioButtons";
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
import { Button, Menu, MenuItem } from "@mui/material"
import { useNavigate } from "react-router-dom";
// import { Tooltip, IconButton } from "@mui/material";
// import HelpIcon from '@mui/icons-material/Help';

function MainPage() {
  // Component State Variables
  const [sliderValue, setSliderValue] = useState<number>(DEFAULT_SLIDER_VAL);
  const [filterFactor, setFilterFactor] = useState<string>("NoFilter");

  // Data State Variables
  const [pastData, setPastData] = useState<DataSeries>();
  const [pastDataUnbiased, setPastDataUnbiased] = useState<DataSeries>();
  const [predictedData, setPredictedData] = useState<DataSeries>();
  const [predictedDataUnbiased, setPredictedDataUnbiased] =
    useState<DataSeries>();
  const navigate = useNavigate();

  async function getPastData() {
    const formattedData = await getPastDataAPICall(filterFactor);

    if (formattedData) {
      setPastData({
        name: "Known Data",
        color: "#2933f2", //blue
        data: formattedData,
      });
    }
  }
  async function getPastDataUnbiased() {
    const formattedData = await getPastDataUnbiasedAPICall(filterFactor);

    if (formattedData) {
      setPastDataUnbiased({
        name: "Known Data (Unbiased)",
        color: "#f72525", //red
        data: formattedData,
      });
    }
  }
  async function predictData() {
    const formattedData = await predictDataAPICall(filterFactor, sliderValue);

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
      filterFactor,
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


  // Add a "HOW TO USE" navigated by a menu button
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  const handleClick = (event:React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };


  return (
    <div>
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
      <RadioButtons
        filterFactor={filterFactor}
        setFilterFactor={setFilterFactor}
      />
      <PredictButton onClick={updatePrediction} />
      <br />
      <br />
      <ExportGraphButton />
      <Button
        variant="contained"
        color="primary"
        onClick={handleClick}
      >
        Menu 
      </Button>

      <Menu
      anchorEl={anchorEl}
      open={Boolean(anchorEl)}
      onClose={handleClose}
    >
      <MenuItem onClick={() => navigate("/guidance")}>How To Use</MenuItem>
    </Menu>
    <div>
    {/* <Tooltip title="The slider is used to adjust the prediction size.">
      <IconButton>
        <HelpIcon className="custom-help-icon" />
      </IconButton>
    </Tooltip> */}
    </div>
  </div>
  );
}

export default MainPage;
