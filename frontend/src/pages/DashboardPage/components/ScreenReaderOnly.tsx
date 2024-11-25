import { Alert, AlertTitle } from '@mui/material';
import { useEffect, useRef } from 'react';
import "./ScreenReaderOnly.css"; 

interface GraphDescriptionProps {
  modeGraphData: {
    average_difference: number;
    total_difference: number;
    past_biased_line: Array<{ value: number }>;
    predicted_biased_line: Array<{ value: number }>;
    predicted_unbiased_line: Array<{ value: number }>;
  };
  mode: string;
  filterGender: string;
  filterRace: string;
}

export const GraphDescription = ({
  modeGraphData,
  mode,
  filterGender,
  filterRace
}: GraphDescriptionProps) => {
  const alertRef = useRef<HTMLDivElement>(null); 

  if (!modeGraphData) return null;

  const metricType = mode === "0" ? "transactions" : "revenue";

  const calculatePercentageChange = () => {
    const latestBiased = modeGraphData.predicted_biased_line[modeGraphData.predicted_biased_line.length - 1]?.value || 0;
    const latestUnbiased = modeGraphData.predicted_unbiased_line[modeGraphData.predicted_unbiased_line.length - 1]?.value || 0;
    const percentChange = ((latestUnbiased - latestBiased) / latestBiased * 100).toFixed(1);
    return percentChange;
  };

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
    >

      <Alert
        ref={alertRef}               
        role="alert"                 
        aria-live="polite"        
        aria-labelledby="graph-description-title" 
        aria-atomic="true"         
        tabIndex={-1}               
      >
        <AlertTitle id="graph-description-title">Graph Analysis Overview</AlertTitle> 
        {/* Using aria labels here so it speaks it, sr-only makes it tiny and renders it so that only screen readers can hear  */}
        <div 
          id="summary-stats" 
          aria-labelledby="summary-stats" 
          role="region"
          tabIndex={0}
        >
          <h3 id="summary-stats">Summary Statistics</h3>
          <p>
            The average {metricType} difference is {modeGraphData.average_difference.toLocaleString()}.
            The total {metricType} difference is {modeGraphData.total_difference.toLocaleString()}.
          </p>
        </div>
        <div 
          id="trend-analysis" 
          aria-labelledby="trend-analysis" 
          role="region"
          tabIndex={0}
        >
          <h3 id="trend-analysis">Trend Analysis</h3>
          <p>
            {modeGraphData.past_biased_line.length > 0 &&
              `Historical ${metricType} data started at ${modeGraphData.past_biased_line[0]?.value.toLocaleString()}. `}
            {modeGraphData.predicted_biased_line.length > 0 &&
              `With current biases, ${metricType} are predicted to reach ${modeGraphData.predicted_biased_line[modeGraphData.predicted_biased_line.length - 1]?.value.toLocaleString()}. `}
            {modeGraphData.predicted_unbiased_line.length > 0 &&
              `Without biases, ${metricType} could reach ${modeGraphData.predicted_unbiased_line[modeGraphData.predicted_unbiased_line.length - 1]?.value.toLocaleString()}, representing a ${calculatePercentageChange()}% change.`}
          </p>
        </div>
        <div 
          id="applied-filters" 
          aria-labelledby="applied-filters" 
          role="region"
          tabIndex={0}
        >
          <h3 id="applied-filters">Applied Filters</h3>
          <p>
            Currently showing data
            {filterGender !== "NoFilter" ? ` filtered by Gender: ${filterGender}` : ''}
            {filterRace !== "NoFilter"
              ? `${filterGender !== "NoFilter" ? ' and' : ' filtered by'} Race: ${filterRace}`
              : ''}
            {filterGender === "NoFilter" && filterRace === "NoFilter" ? " with no filters applied" : ''}
          </p>
        </div>
      </Alert>
    </div>
  );
};

export default GraphDescription;
