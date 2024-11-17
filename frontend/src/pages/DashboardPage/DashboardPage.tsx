import "./DashboardPage.css";
import { useEffect, useState } from "react";
import Slider, { DEFAULT_SLIDER_VAL } from "./components/Slider";
import GenderDropdownFilter from "./components/GenderDropdownFilter";
import RaceDropdownFilter from "./components/RaceDropdownFilter";
import PredictButton from "./components/PredictButton";
import Graph from "./components/Graph";
import {
  getPastDataAPICall,
  getPastDataUnbiasedAPICall,
  predictDataAPICall,
  predictDataUnbiasedAPICall,
} from "../../ApiCalls";
import { DataSeries } from "../../types";
import ExportGraphButton from "./components/ExportGraphButton";
import { Button, Menu, MenuItem, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";
import RadioButtons from "./components/RadioButtons";
import InfoTooltip from "./components/InfoTooltip";
import AverageBigNumber from "./components/AverageBigNumber";

function DashboardPage() {
  const navigate = useNavigate();

  // Component State Variables
  const [sliderValue, setSliderValue] = useState<number>(DEFAULT_SLIDER_VAL);
  const [mode, setMode] = useState<string>("0");
  const [filterGender, setFilterGender] = useState<string>("NoFilter");
  const [filterRace, setFilterRace] = useState<string>("NoFilter");
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  // Data State Variables
  const [pastData, setPastData] = useState<DataSeries>();
  const [pastDataUnbiased, setPastDataUnbiased] = useState<DataSeries>();
  const [predictedData, setPredictedData] = useState<DataSeries>();
  const [predictedDataUnbiased, setPredictedDataUnbiased] =
    useState<DataSeries>();

  function formatNumberForDisplay(num: number): string {
    if (num >= 1_000_000_000) {
      const billions = num / 1_000_000_000;
      return billions >= 100 ? `${Math.round(billions)}B` : `${billions.toFixed(1).replace(/\.0$/, '')}B`;
    } else if (num >= 1_000_000) {
      const millions = num / 1_000_000;
      return millions >= 100 ? `${Math.round(millions)}M` : `${millions.toFixed(1).replace(/\.0$/, '')}M`;
    } else if (num >= 1_000) {
      const thousands = num / 1_000;
      return thousands >= 100 ? `${Math.round(thousands)}K` : `${thousands.toFixed(1).replace(/\.0$/, '')}K`;
    } else {
      return num.toString();
    }
  }

  async function getPastData() {
    const formattedData = await getPastDataAPICall(
      [filterGender, filterRace],
      mode
    );

    if (formattedData) {
      setPastData({
        name: "Known Data",
        color: "#2933f2",
        data: formattedData,
      });
    }
  }
  async function getPastDataUnbiased() {
    const formattedData = await getPastDataUnbiasedAPICall(
      [filterGender, filterRace],
      mode
    );

    if (formattedData) {
      setPastDataUnbiased({
        name: "Known Data (Unbiased)",
        color: "#f72525", //red
        data: formattedData,
      });
    }
  }
  async function predictData() {
    const formattedData = await predictDataAPICall(
      [filterGender, filterRace],
      sliderValue,
      mode
    );

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

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <div id="grid-container">
      <header>
        <span style={{ display: "flex" }}>
          <h1 style={{ marginRight: "40px" }}>Showing data for</h1>
          <RadioButtons mode={mode} setMode={setMode}></RadioButtons>
        </span>

        <div id="menu-container">
          <Button
            variant="contained"
            color="success"
            onClick={handleClick}
            aria-haspopup="true"
            aria-expanded={Boolean(anchorEl)}
            aria-controls="menu"
            aria-label="Open menu"
          >
            Menu
          </Button>
          <Menu
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={handleClose}
            aria-label="Main menu"
          >
            <MenuItem onClick={() => navigate("/guidance")}>
              How To Use
            </MenuItem>
            <MenuItem onClick={() => navigate("/upload-dataset")}>
              Upload Dataset
            </MenuItem>
          </Menu>
        </div>
      </header>

      <Box
        bgcolor="beige"
        display="flex"
        justifyContent="center"
        alignItems="center"
      >
        <Graph
          pastData={pastData}
          pastDataUnbiased={pastDataUnbiased}
          predictedData={predictedData}
          predictedDataUnbiased={predictedDataUnbiased}
        />
      </Box>

      <Box bgcolor="cornsilk" padding="40px">
        <AverageBigNumber></AverageBigNumber>

        <span style={{ display: "flex", justifyContent: "space-between" }}>
          <h2>Prediction Size:</h2>
          <InfoTooltip
            title="The slider is used to adjust the prediction size. Longer timeframe when slider is on the right."
            ariaLabel="Help with prediction size slider"
          ></InfoTooltip>
        </span>

        <Slider
          sliderValue={sliderValue}
          setSliderValue={setSliderValue}
          aria-labelledby="prediction-size-label"
        />

        <span style={{ display: "flex", justifyContent: "space-between" }}>
          <h2>Filters:</h2>
          <InfoTooltip
            title="Select the filters below to investigate a subset of the dataset."
            ariaLabel="Help with filters"
          ></InfoTooltip>
        </span>
        <GenderDropdownFilter
          // filterFactor={filterFactor}
          // setFilterFactor={setFilterFactor}
          aria-label="Gender filter options"
          onSelectChange={(value: string) => setFilterGender(value)}
        />
        <RaceDropdownFilter
          aria-label="Race filter options"
          onSelectChange={(value: string) => setFilterRace(value)}
        />

        <span
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginTop: "40px",
          }}
        >
          <PredictButton
            onClick={updatePrediction}
            aria-label="Update prediction"
          />
          <ExportGraphButton aria-label="Export graph" />
        </span>
      </Box>
    </div>
  );
}
export default DashboardPage;
