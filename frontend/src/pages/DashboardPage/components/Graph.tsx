import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    ReferenceLine,
    Label,
} from "recharts";
import {DataSeries} from "../../../types";
import {CYAN, PINK} from "../DashboardPage";
import Typography from "@mui/material/Typography";
import {Box} from "@mui/material";

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
        <div>
            <Box display="flex" flexDirection="column" alignItems="center">
                <Box width="900px">
                    <Typography component="h1" variant="h3" align="center">
                        Transactions {mode == "0" ? "Transaction Volume" : "Cash Flow"} Over
                        Time
                    </Typography>
                </Box>
                <Box display="flex" justifyContent="center">
                    <p style={{color: CYAN, marginRight: "30px"}}>Biased
                        Data</p>
                    <p style={{color: PINK}}>Unbiased Data</p>
                </Box>
            </Box>

            {/*<span*/}
            {/*  style={{*/}
            {/*    display: "flex",*/}
            {/*    justifyContent: "center",*/}
            {/*    fontWeight: "bold",*/}
            {/*  }}*/}
            {/*>*/}
            {/*  <Typography component="h2" variant="h2">*/}
            {/*    Cash App Transactions*/}
            {/*  </Typography>*/}
            {/*  <p style={{ color: CYAN, marginRight: "30px" }}>Biased Data</p>*/}
            {/*  <p style={{ color: PINK }}>Unbiased Data</p>*/}
            {/*</span>*/}

            <div id="graph-canvas">
                {pastData == undefined ? (
                    <h1>Loading...</h1>
                ) : (
                    <LineChart
                        width={900}
                        height={600}
                        margin={{bottom: 50, left: 70, right: 50}}
                    >
                        <CartesianGrid strokeDasharray="3 3"/>
                        <XAxis
                            dataKey="date"
                            scale="time"
                            type="number"
                            tickFormatter={dateFormatter}
                            domain={[startDate, endDate]}
                            ticks={monthTicks}
                        >
                            <Label
                                value={"Date (Months)"}
                                style={{
                                    fill: "black",
                                    transform: "translate(0, 30px)",
                                }}
                            />
                        </XAxis>

                        <YAxis dataKey="value">
                            <Label
                                value={mode == "0" ? "Transaction Volume" : "Cash Flow ($)"}
                                style={{
                                    fill: "black",
                                    rotate: "270deg",
                                    textAnchor: "middle",
                                    transform: "translate(-350px, -225px)",
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
                                    offset: 10,
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
