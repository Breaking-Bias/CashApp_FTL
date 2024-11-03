import Slider from "@mui/material/Slider";
import Button from "@mui/material/Button";
import { DataEntry, DataSeries } from "../types";
import { useState } from "react";

interface Props {
  setPredictedData: (newValue: DataSeries) => void;
}

const MIN_SLIDER_VAL = 10;
const MAX_SLIDER_VAL = 100;
const DEFAULT_SLIDER_VAL = 30;

function SelectForecastSize({ setPredictedData }: Props) {
  const [sliderValue, setSliderValue] = useState<number>(DEFAULT_SLIDER_VAL);

  async function getPredictedData() {
    const serverURL = process.env.VITE_SERVER_URL;
    const endpoint = `${serverURL}/predictValues`;

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ numPoints: sliderValue }),
      });

      if (!response.ok) {
        throw new Error("Error in response: " + response.statusText);
      }

      const data: DataEntry[] = await response.json();
      const formattedData: { date: Date; value: number }[] = data.map(
        (entry) => ({
          date: new Date(entry.date),
          value: entry.value,
        })
      );

      const predictedDataSeries: DataSeries = {
        name: "Forecasted Data",
        color: "red",
        data: formattedData,
      };

      setPredictedData(predictedDataSeries);
    } catch (error) {
      console.error("Error:", error);
    }
  }

  function handleSliderChange(
    _event: Event,
    value: number | number[] | null,
    _activeThumb: number
  ) {
    setSliderValue(value as number);
  }

  function handleButtonPress() {
    console.log(sliderValue);
    getPredictedData();
  }

  return (
    <div>
      <div title="slider-container">
        <Slider
          data-testid="forecast-slider"
          defaultValue={50}
          min={MIN_SLIDER_VAL}
          max={MAX_SLIDER_VAL}
          aria-label="Default"
          valueLabelDisplay="auto"
          value={sliderValue}
          onChange={handleSliderChange}
        />
      </div>
      <div title="button-container">
        <Button
          variant="contained"
          data-testid="forecast-button"
          onClick={handleButtonPress}
        >
          Make Forecast
        </Button>
      </div>
    </div>
  );
}

export default SelectForecastSize;
