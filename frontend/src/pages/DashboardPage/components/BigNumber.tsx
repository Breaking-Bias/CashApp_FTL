import {Box} from "@mui/material";
import { v4 as uuidv4 } from 'uuid';

interface Props {
    value: string;
    averageOrTotal: "daily" | "total";
    revenueOrTransactions: string;
    forExport?: boolean
}

export default function BigNumber({
                                      value,
                                      averageOrTotal,
                                      revenueOrTransactions,
                                      forExport = false,
                                  }: Props) {
    const exportId = forExport ? `big-number-${uuidv4()}` : undefined;
    return (
            <Box display="flex" alignItems="center"
                 justifyContent="space-evenly" id={exportId}>
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
                </p>
            </Box>
    );
}
