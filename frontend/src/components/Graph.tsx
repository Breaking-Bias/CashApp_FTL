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

const series = [
  {
    name: "Known Data",
    color: "blue",
    data: [
      { date: new Date(2023, 7, 1), value: 2 },
      { date: new Date(2023, 7, 2), value: 7 },
      { date: new Date(2023, 7, 3), value: 5 },
    ],
  },
  {
    name: "Predicted Data",
    color: "red",
    data: [
      { date: new Date(2023, 7, 4), value: 1 },
      { date: new Date(2023, 7, 5), value: 3 },
      { date: new Date(2023, 7, 6), value: 4 },
    ],
  },
];

const startDate = series[0].data[0].date; // gets the first data across all data
const endDate = series.slice(-1)[0].data.slice(-1)[0].date; // gets the last date across all data

const dateFormatter = (date: Date) => new Date(date).toLocaleDateString();

export default function App() {
  const [knownData, setKnownData] = useState([]);

  async function getKnownData() {
    const serverURL = import.meta.env.VITE_SERVER_URL;
    const endpoint = serverURL + "/getOriginalData";
    console.log(endpoint);

    try {
      // make the request
      const response = await fetch(endpoint);

      // catch errors in fetch response
      if (!response.ok) {
        throw new Error("Error in response:" + response.statusText);
      }

      // convert the data to json
      const data = await response.json();

      setKnownData(data);
    } catch (error) {
      console.error("Error:", error);
    }
  }

  useEffect(() => {
    getKnownData();
  }, []);

  useEffect(() => {
    console.log(knownData);
  }, [knownData]);

  return (
    <LineChart width={800} height={500}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis
        angle={-45}
        textAnchor="end"
        dataKey="date"
        scale="time"
        type="number"
        tickFormatter={dateFormatter}
        domain={[startDate.getTime(), endDate.getTime()]}
      />
      <YAxis dataKey="value" />
      <Tooltip />
      <Legend />
      {series.map((s) => (
        <Line
          dataKey="value"
          data={s.data}
          name={s.name}
          stroke={s.color}
          key={s.name}
        />
      ))}
    </LineChart>
  );
}
