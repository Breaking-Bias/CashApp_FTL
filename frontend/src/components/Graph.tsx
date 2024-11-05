import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
import { DataEntry, DataSeries } from "../types";

const dateFormatter = (date: Date) => new Date(date).toLocaleDateString();

interface Props {
  predictedData: DataSeries | undefined;
}

function Graph({ predictedData }: Props) {
  // Explicitly set the type for knownData
  const [knownData, setKnownData] = useState<DataSeries>();

  async function getKnownData() {
    const serverURL = import.meta.env.VITE_SERVER_URL;
    const endpoint = `${serverURL}/getPastData`;

    try {
      const response = await fetch(endpoint);

      // Catch errors in fetch response
      if (!response.ok) {
        throw new Error("Error in response: " + response.statusText);
      }

      // Convert the data to JSON
      const data: DataEntry[] = await response.json();
      const formattedData: { date: Date; value: number }[] = data.map(
        (entry) => ({
          date: new Date(entry.date),
          value: entry.value,
        })
      );

      const knownDataSeries: DataSeries = {
        name: "Known Data",
        color: "blue",
        data: formattedData,
      };

      // Ensure that temp is of type DataSeries[]
      setKnownData(knownDataSeries);
    } catch (error) {
      console.error("Error:", error);
    }
  }

  useEffect(() => {
    getKnownData();
  }, []);

  function getGraphDomain() {
    if (knownData) {
      const start = knownData.data[0].date.getTime();

      let end;
      if (predictedData) {
        end = predictedData.data.slice(-1)[0].date.getTime();
      } else {
        end = knownData.data.slice(-1)[0].date.getTime();
      }

      return [start, end];
    }
  }

  return (
    <div>
      {knownData == undefined ? (
        <h1>Loading...</h1>
      ) : (
        <LineChart width={800} height={500}>
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
          <Tooltip />
          <Legend />

          <Line
            type="monotone"
            dataKey="value"
            data={knownData.data}
            name={knownData.name}
            stroke={knownData.color}
          />

          {predictedData && (
            <Line
              type="monotone"
              dataKey="value"
              data={predictedData.data}
              name={predictedData.name}
              stroke={predictedData.color}
            />
          )}
        </LineChart>
      )}
    </div>
  );
}

export default Graph;
