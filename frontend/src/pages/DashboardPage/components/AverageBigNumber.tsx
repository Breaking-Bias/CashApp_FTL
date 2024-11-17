import { Box } from "@mui/material";
import InfoTooltip from "./InfoTooltip";

export default function AverageBigNumber() {
  return (
    <Box display="flex">
      <p
        style={{
          fontSize: "5rem",
          fontWeight: "bold",
          color: "black",
          margin: 0,
        }}
      >
        $10B
      </p>
      <p>
        average <br /> revenue
      </p>
      <InfoTooltip title="" ariaLabel="" />
    </Box>
  );
}
