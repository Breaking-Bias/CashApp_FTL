import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  ReferenceLine,
  Label,
} from "recharts";
import { DataSeries } from "../../../types";
import { CYAN, PINK } from "../DashboardPage";
import Typography from "@mui/material/Typography";
import { Box } from "@mui/material";


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

  const generateMonthTicks = (startDate: Date, endDate: Date) => {
    const ticks = [];
    const current = new Date(startDate);
    current.setDate(1);
    current.setMonth(current.getMonth() + 1);

    while (current <= endDate) {
      ticks.push(current.getTime());
      current.setMonth(current.getMonth() + 1);
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

  const [startDate, endDate] = getGraphDomain();
  const monthTicks = generateMonthTicks(new Date(startDate), new Date(endDate));

  return (
    <div>
      <Box display="flex" flexDirection="column" alignItems="center">
        <Box width="900px">
          <Typography 
            component="h1" 
            variant="h4" 
            align="center"
            sx={{
              fontFamily: "'Inter', -apple-system, sans-serif",
              fontWeight: 600,
              fontSize: '1.75rem',
              color: '#1a2027',
              marginBottom: '1rem'
            }}
          >
            {mode === "0" ? "Transaction Volume" : "Cash Flow"} Over Time
          </Typography>
        </Box>
        <Box display="flex" justifyContent="center" sx={{ marginBottom: '2rem' }}>
          <Typography 
            sx={{ 
              color: CYAN, 
              marginRight: '30px', 
              fontWeight: 600,
              fontFamily: "'Inter', -apple-system, sans-serif",
              fontSize: '0.9rem'
            }}
          >
            Biased Data
          </Typography>
          <Typography 
            sx={{ 
              color: PINK, 
              fontWeight: 600,
              fontFamily: "'Inter', -apple-system, sans-serif",
              fontSize: '0.9rem'
            }}
          >
            Unbiased Data
          </Typography>
        </Box>
      </Box>

      <div id="graph-canvas">
        {pastData === undefined ? (
          <Typography 
            variant="h6" 
            sx={{ 
              fontFamily: "'Inter', -apple-system, sans-serif",
              fontWeight: 500 
            }}
          >
            Loading...
          </Typography>
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
              tick={{ 
                fontFamily: "'Inter', -apple-system, sans-serif",
                fontSize: 12,
                fontWeight: 500 
              }}
            >
              <Label
                value="Date (Months)"
                style={{
                  fill: "#1a2027",
                  transform: "translate(0, 30px)",
                  fontFamily: "'Inter', -apple-system, sans-serif",
                  fontSize: 13,
                  fontWeight: 500
                }}
              />
            </XAxis>

            <YAxis dataKey="value" tick={{ 
              fontFamily: "'Inter', -apple-system, sans-serif",
              fontSize: 12,
              fontWeight: 500 
            }}>
              <Label
                value={mode === "0" ? "Transaction Volume" : "Cash Flow ($)"}
                style={{
                  fill: "#1a2027",
                  rotate: "270deg",
                  textAnchor: "middle",
                  transform: "translate(-350px, -225px)",
                  fontFamily: "'Inter', -apple-system, sans-serif",
                  fontSize: 13,
                  fontWeight: 500
                }}
                position="outside"
              />
            </YAxis>

            <Line
              dot={false}
              type="monotone"
              dataKey="value"
              data={pastData.data}
              name={pastData.name}
              stroke={pastData.color}
              strokeWidth={2}
            />

            {pastDataUnbiased && (
              <Line
                dot={false}
                type="monotone"
                dataKey="value"
                data={pastDataUnbiased.data}
                name={pastDataUnbiased.name}
                stroke={pastDataUnbiased.color}
                strokeWidth={2}
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
                strokeWidth={2}
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
                strokeWidth={2}
              />
            )}

            {predictedData && (
              <ReferenceLine
                x={predictedData.data[0].date.getTime()}
                label={{
                  value: "Present",
                  position: "insideTopRight",
                  style: {
                    fontFamily: "'Inter', -apple-system, sans-serif",
                    fontSize: 12,
                    fontWeight: 500
                  }
                }}
                stroke="gray"
              />
            )}
          </LineChart>
        )}
      </div>
    </div>
  );
}

export default Graph;