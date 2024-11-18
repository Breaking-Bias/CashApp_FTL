import { Box } from "@mui/material";
import InfoTooltip from "./InfoTooltip";

interface Props {
  value: string;
  averageOrTotal: "average" | "total";
  revenueOrTransactions: string;
}

export default function BigNumber({
  value,
  averageOrTotal,
  revenueOrTransactions,
}: Props) {
  return (
    <Box display="flex" alignItems="center" justifyContent="space-evenly">
      <p
        style={{
          fontSize: "4rem",
          fontWeight: "bold",
          color: "black",
          margin: 0,
        }}
      >
        {value}
      </p>
      <p>
        {averageOrTotal}
        <br />
        {revenueOrTransactions == "0" ? "transactions" : "revenue"}
      </p>
      <InfoTooltip
        title={`The ${averageOrTotal} difference between biased and unbiased ${
          revenueOrTransactions == "0" ? "transactions" : "revenue"
        }.`}
        ariaLabel={`Help with ${averageOrTotal} ${
          revenueOrTransactions == "0" ? "transactions" : "revenue"
        }`}
      />
    </Box>
  );
}
