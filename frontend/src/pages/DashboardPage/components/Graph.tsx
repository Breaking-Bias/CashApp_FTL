import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
  ReferenceLine,
  Label,
} from "recharts";
import { DataSeries } from "../../../types";

// const dateFormatter = (date: Date) => new Date(date).toLocaleDateString();

interface Props {
  mode: string;
  pastData: DataSeries | undefined;
  pastDataUnbiased?: DataSeries | undefined;
  predictedData?: DataSeries | undefined;
  predictedDataUnbiased?: DataSeries | undefined;
}

function Graph({
  mode,
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
    return [0, 0];
  }

  // Generate ticks for the first day of each month
  const generateMonthTicks = (startDate: Date, endDate: Date) => {
    const ticks = [];
    const current = new Date(startDate);
    current.setDate(1);
    current.setMonth(current.getMonth() + 1); // Move to the next month

    // Generate ticks for the first day of each month within the range
    while (current <= endDate) {
      ticks.push(current.getTime());
      current.setMonth(current.getMonth() + 1); // Move to the next month
    }

    return ticks;
  };

  const dateFormatter = (tick: number) => {
    const date = new Date(tick);
    return date.toLocaleDateString("en-US", {
      month: "short",
      year: "numeric",
    });
  };

  // Get the domain from pastData and predictedData
  const [startDate, endDate] = getGraphDomain();
  const monthTicks = generateMonthTicks(new Date(startDate), new Date(endDate));

  return (
    <div id="graph-canvas">
      {pastData == undefined ? (
        <h1>Loading...</h1>
      ) : (
        <LineChart
          width={900}
          height={600}
          margin={{ bottom: 50, left: 70, right: 50 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            dataKey="date"
            scale="time"
            type="number"
            tickFormatter={dateFormatter}
            domain={[startDate, endDate]}
            ticks={monthTicks}
          >
            <Label
              value={"Time"}
              style={{
                fill: "black",
                transform: "translate(0, 30px)",
              }}
            />
          </XAxis>

          <YAxis dataKey="value">
            <Label
              value={mode == "0" ? "Number of Transactions" : "Cash Flow ($)"}
              style={{
                fill: "black",
                rotate: "270deg",
                textAnchor: "middle",
                transform: "translate(-350px, -250px)",
              }}
              position="outside"
              offset={-20}
            />
          </YAxis>

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
