import React, { useEffect, useRef } from "react";
import { Alert, AlertTitle } from "@mui/material";
import { GraphAnalysisService } from "../../../services/GraphAnalysisService";
import "./ScreenReaderOnly.css";

//Created two interfaces, this satisfied the L in solid

interface ModeGraphData {
  average_difference: number;
  total_difference: number;
  past_biased_line: Array<{ value: number }>;
  predicted_biased_line: Array<{ value: number }>;
  predicted_unbiased_line: Array<{ value: number }>;
}
//Small and focused interfaces

interface GraphDescriptionProps {
  modeGraphData: ModeGraphData;
  mode: string;
  filterGender: string;
  filterRace: string;
}
// divided up the three components, ie the summary stats, trend analalysis (percentage logic) and details about the filters
const SummaryStatistics: React.FC<{
  metricType: string;
  averageDifference: number;
  totalDifference: number;
}> = ({ metricType, averageDifference, totalDifference }) => (
  <div
    id="summary-stats"
    aria-labelledby="summary-stats"
    role="region"
    tabIndex={0}
  >
    <h3 id="summary-stats">Summary Statistics</h3>
    <p>
      The average {metricType} difference is{" "}
      {averageDifference.toLocaleString()}. The total {metricType} difference is{" "}
      {totalDifference.toLocaleString()}.
    </p>
  </div>
);

const TrendAnalysis: React.FC<{
  metricType: string;
  pastBiasedLine: Array<{ value: number }>;
  predictedBiasedLine: Array<{ value: number }>;
  predictedUnbiasedLine: Array<{ value: number }>;
}> = ({
  metricType,
  pastBiasedLine,
  predictedBiasedLine,
  predictedUnbiasedLine,
}) => {
  const percentChange = GraphAnalysisService.calculatePercentageChange(
    predictedBiasedLine,
    predictedUnbiasedLine
  );

  // I'm sure there's an easier way, but this is to call the logic service here, so the final return statement is cleaner

  return (
    <div
      id="trend-analysis"
      aria-labelledby="trend-analysis"
      role="region"
      tabIndex={0}
    >
      <h3 id="trend-analysis">Trend Analysis</h3>
      <p>
        {pastBiasedLine.length > 0 &&
          `Historical ${metricType} data started at ${pastBiasedLine[0]?.value.toLocaleString()}. `}
        {predictedBiasedLine.length > 0 &&
          `With current biases, ${metricType} are predicted to reach ${predictedBiasedLine[
            predictedBiasedLine.length - 1
          ]?.value.toLocaleString()}. `}
        {predictedUnbiasedLine.length > 0 &&
          `Without biases, ${metricType} could reach ${predictedUnbiasedLine[
            predictedUnbiasedLine.length - 1
          ]?.value.toLocaleString()}, representing a ${percentChange}% change.`}
      </p>
    </div>
  );
};

const AppliedFilters: React.FC<{
  filterGender: string;
  filterRace: string;
}> = ({ filterGender, filterRace }) => (
  <div
    id="applied-filters"
    aria-labelledby="applied-filters"
    role="region"
    tabIndex={0}
  >
    <h3 id="applied-filters">Applied Filters</h3>
    <p>
      Currently showing data{" "}
      {GraphAnalysisService.formatFilterDescription(filterGender, filterRace)}
    </p>
  </div>
);
export const GraphDescription: React.FC<GraphDescriptionProps> = ({
  modeGraphData,
  mode,
  filterGender,
  filterRace,
}) => {
  const alertRef = useRef<HTMLDivElement>(null); //Just being careful

  if (!modeGraphData) return null;
  const metricType = GraphAnalysisService.getMetricType(mode);

  useEffect(() => {
    if (alertRef.current) {
      alertRef.current.focus();
    }
  }, [modeGraphData]);

  return (
    <div
      className="sr-only"
      role="region"
      aria-label="Graph Analysis Details"
      data-testid="test-alert"
    >
      <Alert
        ref={alertRef}
        role="alert"
        aria-live="polite"
        aria-labelledby="graph-description-title"
        aria-atomic="true"
        tabIndex={-1}
      >
        <AlertTitle id="graph-description-title">
          Graph Analysis Overview
        </AlertTitle>

        <SummaryStatistics
          metricType={metricType}
          averageDifference={modeGraphData.average_difference}
          totalDifference={modeGraphData.total_difference}
        />

        <TrendAnalysis
          metricType={metricType}
          pastBiasedLine={modeGraphData.past_biased_line}
          predictedBiasedLine={modeGraphData.predicted_biased_line}
          predictedUnbiasedLine={modeGraphData.predicted_unbiased_line}
        />

        <AppliedFilters filterGender={filterGender} filterRace={filterRace} />
      </Alert>
    </div>
  );
};

export default GraphDescription;
