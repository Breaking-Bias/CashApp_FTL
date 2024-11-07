import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
  ReferenceLine,
} from "recharts";
import { DataSeries } from "../types";

const dateFormatter = (date: Date) => new Date(date).toLocaleDateString();

interface Props {
  pastData: DataSeries | undefined;
  pastDataUnbiased: DataSeries | undefined;
  predictedData: DataSeries | undefined;
  predictedDataUnbiased: DataSeries | undefined;
}

function Graph({
  pastData,
  pastDataUnbiased,
  predictedData,
  predictedDataUnbiased,
}: Props) {
  function getGraphDomain() {
    if (pastData) {
      const start = pastData.data[0].date.getTime();

      let end;
      if (predictedData) {
        end = predictedData.data.slice(-1)[0].date.getTime();
      } else {
        end = pastData.data.slice(-1)[0].date.getTime();
      }

      return [start, end];
    }
  }

  return (
    <div id="graph-canvas">
      {pastData == undefined ? (
        <h1>Loading...</h1>
      ) : (
        <LineChart width={800} height={500} margin={{ bottom: 50 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            angle={-45}
            textAnchor="end"
            dataKey="date"
            scale="time"
            type="number"
            tickFormatter={dateFormatter}
            domain={getGraphDomain()}
          />
          <YAxis dataKey="value" />
          <Legend layout="horizontal" verticalAlign="top" />

          <Line
            dot={false}
            type="monotone"
            dataKey="value"
            data={pastData.data}
            name={pastData.name}
            stroke={pastData.color}
          />

          {pastDataUnbiased && (
            <Line
              dot={false}
              type="monotone"
              dataKey="value"
              data={pastDataUnbiased.data}
              name={pastDataUnbiased.name}
              stroke={pastDataUnbiased.color}
            />
          )}

          {predictedData && (
            <Line
              dot={false}
              type="monotone"
              dataKey="value"
              data={predictedData.data}
              name={predictedData.name}
              stroke={predictedData.color}
            />
          )}

          {predictedDataUnbiased && (
            <Line
              dot={false}
              type="monotone"
              dataKey="value"
              data={predictedDataUnbiased.data}
              name={predictedDataUnbiased.name}
              stroke={predictedDataUnbiased.color}
            />
          )}

          {predictedData && (
            <ReferenceLine
              x={predictedData.data[0].date.getTime()}
              label={{
                value: "Present",
                position: "insideTopRight",
                offset: 10,
              }}
              stroke="gray"
            />
          )}
        </LineChart>
      )}
    </div>
  );
}

export default Graph;
