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

interface DataSeries {
  name: string;
  color: string;
  data: any[];
}

const dateFormatter = (date: Date) => new Date(date).toLocaleDateString();

export default function App() {
  const [knownData, setKnownData] = useState<DataSeries[]>([]);

  async function getKnownData() {
    const serverURL = import.meta.env.VITE_SERVER_URL;
    const endpoint = serverURL + "/getOriginalData";

    try {
      const response = await fetch(endpoint);

      // catch errors in fetch response
      if (!response.ok) {
        throw new Error("Error in response:" + response.statusText);
      }

      // convert the data to json
      const data = await response.json();
      const formattedData: any[] = [];

      data.forEach((entry: any) => {
        formattedData.push({ date: new Date(entry.date), value: entry.value });
      });

      const temp: DataSeries = {
        name: "Known Data",
        color: "blue",
        data: formattedData,
      };
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
      {knownData.length == 0 ? (
        <h1>loading</h1>
      ) : (
        <div>
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
                knownData[0].data[0].date.getTime(), // gets the first date across all data
                knownData.slice(-1)[0].data.slice(-1)[0].date.getTime(), // gets the last date across all data
              ]}
            />
            <YAxis dataKey="value" />
            <Tooltip />
            <Legend />
            {knownData.map((s) => (
              <Line
                dataKey="value"
                data={s.data}
                name={s.name}
                stroke={s.color}
                key={s.name}
              />
            ))}
          </LineChart>
        </div>
      )}
    </div>
  );
}

export default Graph;