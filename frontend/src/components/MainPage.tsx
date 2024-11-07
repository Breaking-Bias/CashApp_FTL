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

function MainPage() {
  // Component State Variables
  const [sliderValue, setSliderValue] = useState<number>(DEFAULT_SLIDER_VAL);
  const [filterFactor, setFilterFactor] = useState<string>("noFilter");

  // Data State Variables
  const [pastData, setPastData] = useState<DataSeries>();
  const [pastDataUnbiased, setPastDataUnbiased] = useState<DataSeries>();
  const [predictedData, setPredictedData] = useState<DataSeries>();
  const [predictedDataUnbiased, setPredictedDataUnbiased] =
    useState<DataSeries>();

  async function getPastData() {
    const formattedData = await getPastDataAPICall(filterFactor);

    if (formattedData) {
      setPastData({
        name: "Known Data",
        color: "blue",
        data: formattedData,
      });
    }
  }
  async function getPastDataUnbiased() {
    const formattedData = await getPastDataUnbiasedAPICall(filterFactor);

    if (formattedData) {
      setPastDataUnbiased({
        name: "Known Data (Unbiased)",
        color: "red",
        data: formattedData,
      });
    }
  }
  async function predictData() {
    const formattedData = await predictDataAPICall(filterFactor, sliderValue);

    if (formattedData) {
      setPredictedData({
        name: "Predicted Data",
        color: "green",
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
        color: "purple",
        data: formattedData,
      });
    }
  }

  function updatePrediction() {
    getPastDataUnbiased();
    predictData();
    predictDataUnbiased();
  }

  useEffect(() => {
    getPastData();
  }, []);

  return (
    <div>
      <Graph
        pastData={pastData}
        pastDataUnbiased={pastDataUnbiased}
        predictedData={predictedData}
        predictedDataUnbiased={predictedDataUnbiased}
      />
      <Slider sliderValue={sliderValue} setSliderValue={setSliderValue} />
      <RadioButtons
        filterFactor={filterFactor}
        setFilterFactor={setFilterFactor}
      />
      <PredictButton onPress={updatePrediction} />
    </div>
  );
}

export default MainPage;
