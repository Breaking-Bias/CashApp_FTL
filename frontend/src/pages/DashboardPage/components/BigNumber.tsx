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
        <Box aria-live="polite" display="flex" alignItems="center" justifyContent="space-evenly">
            <p
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
            <p>
                Potential&nbsp;
                {averageOrTotal}
                <br/>
                {revenueOrTransactions == "0" ? "transaction volume" : "cash-flow"}
                &nbsp;incr.
            </p>
        </Box>
    );
}
