// components/ScreenReaderOnly/index.tsx
import React from 'react';

type ScreenReaderOnlyProps = {
  as?: 'div' | 'span' | 'section' | 'article' | 'aside' | 'main';
  children: React.ReactNode;
  className?: string;
} & Omit<React.HTMLAttributes<HTMLElement>, 'as'>;

export const ScreenReaderOnly = ({ 
  as: Component = 'div',
  children,
  className,
  ...props 
}: ScreenReaderOnlyProps) => {
  return (
    <Component
      {...props}
      className={`sr-only ${className || ''}`}
    >
      {children}
    </Component>
  );
};

// GraphDescription component specifically for the dashboard graph
interface GraphDescriptionProps {
  modeGraphData: any; // Replace with your actual type
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
  if (!modeGraphData) return null;

  const metricType = mode === "0" ? "transactions" : "revenue";
  
  const calculatePercentageChange = () => {
    const latestBiased = modeGraphData.predicted_biased_line[modeGraphData.predicted_biased_line.length - 1]?.value || 0;
    const latestUnbiased = modeGraphData.predicted_unbiased_line[modeGraphData.predicted_unbiased_line.length - 1]?.value || 0;
    const percentChange = ((latestUnbiased - latestBiased) / latestBiased * 100).toFixed(1);
    return percentChange;
  };

  return (
    <ScreenReaderOnly>
      <h2>Graph Data Analysis</h2>
      <div>
        <h3>Summary Metrics</h3>
        <p>
          {`The average ${metricType} difference is ${modeGraphData.average_difference.toLocaleString()}.`}
        </p>
        <p>
          {`The total ${metricType} difference is ${modeGraphData.total_difference.toLocaleString()}.`}
        </p>
      </div>
      
      <div>
        <h3>Trend Analysis</h3>
        {modeGraphData.past_biased_line.length > 0 && (
          <p>
            {`Historical ${metricType} data started at ${modeGraphData.past_biased_line[0]?.value.toLocaleString()}.`}
          </p>
        )}
        {modeGraphData.predicted_biased_line.length > 0 && (
          <p>
            {`With current biases, ${metricType} are predicted to reach ${modeGraphData.predicted_biased_line[modeGraphData.predicted_biased_line.length - 1]?.value.toLocaleString()}.`}
          </p>
        )}
        {modeGraphData.predicted_unbiased_line.length > 0 && (
          <p>
            {`Without biases, ${metricType} could reach ${modeGraphData.predicted_unbiased_line[modeGraphData.predicted_unbiased_line.length - 1]?.value.toLocaleString()}, 
            representing a ${calculatePercentageChange()}% change.`}
          </p>
        )}
      </div>

      <div>
        <h3>Applied Filters</h3>
        <p>
          Currently showing data 
          {filterGender !== "NoFilter" && ` filtered by Gender: ${filterGender}`}
          {filterRace !== "NoFilter" && ` ${filterGender !== "NoFilter" ? 'and' : 'filtered by'} Race: ${filterRace}`}
          {filterGender === "NoFilter" && filterRace === "NoFilter" && " with no filters applied"}
        </p>
      </div>
    </ScreenReaderOnly>
  );
};