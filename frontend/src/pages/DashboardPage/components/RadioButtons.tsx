import React from "react";
import Switch from "@mui/material/Switch";
import FormControlLabel from "@mui/material/FormControlLabel";

interface Props {
  mode: string;
  setMode: (newValue: string) => void;
}

// 0 means number of transactions, 1 means value of transactions
function SwitchButtons({ mode, setMode }: Props) {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setMode(event.target.checked ? "1" : "0");
  };

  return (
    <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
      <FormControlLabel
        control={
          <Switch
            checked={mode === "1"} // "1" corresponds to Revenue
            onChange={handleChange}
            aria-label="Switch between Transaction Frequency and Revenue"
          />
        }
        label={mode === "0" ? "Transaction Frequency" : "Revenue"}
      />
    </div>
  );
}

export default SwitchButtons;

