import "../App.css";
import { useEffect, useState } from "react";
import Slider, { DEFAULT_SLIDER_VAL } from "./Slider";
import RadioButtons from "./RadioButtons";
import PredictButton from "./PredictButton";
import Graph from "./Graph";
import { getPastDataAPICall, getPastDataUnbiasedAPICall } from "../ApiCalls";
import { DataSeries } from "../types";

function MainPage() {
  const [sliderValue, setSliderValue] = useState<number>(DEFAULT_SLIDER_VAL);
  const [filterFactor, setFilterFactor] = useState<string>("noFilter");

  // Data State Variables
  const [pastData, setPastData] = useState<DataSeries>();
  const [pastDataUnbiased, setPastDataUnbiased] = useState<DataSeries>();

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

  useEffect(() => {
    getPastData();
  }, []);

  return (
    <div>
      {/* <Graph predictedData={}/> */}
      <Slider sliderValue={sliderValue} setSliderValue={setSliderValue} />
      <RadioButtons
        filterFactor={filterFactor}
        setFilterFactor={setFilterFactor}
      />
      {/* <PredictButton predict={predict} /> */}
    </div>
  );
}

export default MainPage;
