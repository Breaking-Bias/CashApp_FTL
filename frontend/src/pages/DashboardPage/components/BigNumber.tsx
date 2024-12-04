import {Box} from "@mui/material";

interface Props {
    value: string;
    averageOrTotal: "daily" | "total";
    revenueOrTransactions: string;
}

export default function BigNumber({
                                      value,
                                      averageOrTotal,
                                      revenueOrTransactions,
                                  }: Props) {
    return (
            <Box display="flex" alignItems="center"
                 justifyContent="space-evenly">
                {/*TODO: Make this aria label dynamic*/}
                <p aria-label="Potential daily"
                    style={{
                    fontSize: "4rem",
                    fontWeight: "bold",
                    color: "black",
                    margin: 0,
                }}
                >
                    {revenueOrTransactions == "1" && "$"}
                    {value}
                </p>
                <p aria-hidden="true">
                    Potential&nbsp;
                    {averageOrTotal}
                    <br/>
                    {revenueOrTransactions == "0" ? "transaction volume" : "cash-flow"}
                    &nbsp;incr.
                    <br/>
                    {averageOrTotal == "total" ? "over timeframe" : ""}
                </p>
            </Box>
    );
}
