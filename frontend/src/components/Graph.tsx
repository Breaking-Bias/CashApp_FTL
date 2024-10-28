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

interface DataEntry {
  date: string; // THIS CAN BE CHANGED GUYS
  value: number;
}


interface DataSeries {
  name: string;
  color: string;
  data: { date: Date; value: number }[];
}

const dateFormatter = (date: Date) => new Date(date).toLocaleDateString();

function Graph() {
  // Explicitly set the type for knownData
  const [knownData, setKnownData] = useState<DataSeries[]>([]);

  async function getKnownData() {
    const serverURL = import.meta.env.VITE_SERVER_URL;
    const endpoint = `${serverURL}/getOriginalData`;

    try {
      const response = await fetch(endpoint);

      // Catch errors in fetch response
      if (!response.ok) {
        throw new Error("Error in response: " + response.statusText);
      }

      // Convert the data to JSON
      const data: DataEntry[] = await response.json();
      const formattedData: { date: Date; value: number }[] = data.map(entry => ({
        date: new Date(entry.date),
        value: entry.value,
      }));

      const temp: DataSeries = {
        name: "Known Data",
        color: "blue",
        data: formattedData,
      };

      // Ensure that temp is of type DataSeries[]
      setKnownData([temp]);
    } catch (error) {
      console.error("Error:", error);
    }
  }

  useEffect(() => {
    getKnownData();
  }, []);

  return (
    <div>
      {knownData.length === 0 ? (
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
            domain={[
              knownData[0].data[0].date.getTime(),
              knownData[0].data[knownData[0].data.length - 1].date.getTime(),
            ]}
          />
          <YAxis dataKey="value" />
          <Tooltip />
          <Legend />
          {knownData.map((series) => (
            <Line
              key={series.name}
              type="monotone"
              dataKey="value"
              data={series.data}
              name={series.name}
              stroke={series.color}
            />
          ))}
        </LineChart>
      )}
    </div>
  );
}

export default Graph;
