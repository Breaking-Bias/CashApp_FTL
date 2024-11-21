import React from "react";
import Switch from "@mui/material/Switch";
import FormControlLabel from "@mui/material/FormControlLabel";

interface Props {
  mode: string;
  setMode: (newValue: string) => void;
}

function SwitchButtons({ mode, setMode }: Props) {
  const handleChange = () => {
    setMode(mode === "0" ? "1" : "0");
  };

  // Ensure that the "tabbing" and "Enter" key toggle work together
  const handleKeyDown = (event: React.KeyboardEvent) => {
    if (event.key === "Enter" || event.key === " ") {
      // Toggle between "0" and "1" on Enter or Space
      setMode(mode === "0" ? "1" : "0");
    }
  };

  return (
    <div>
      {/* Revenue Switch */}
      <FormControlLabel
        control={
          <Switch
            id="revenue-switch"
            checked={mode === "1"}
            onChange={handleChange}
            onKeyDown={handleKeyDown} // Add onKeyDown for keyboard interactions (Enter/Space)
            tabIndex={1} // Ensure this is focusable after the first switch
            aria-label="Revenue"
          />
        }
        label="Revenue"
      />

      {/* Transaction Frequency Switch */}
      <FormControlLabel
        control={
          <Switch
            id="transactions-switch"
            checked={mode === "0"}
            onChange={handleChange}
            onKeyDown={handleKeyDown} // Add onKeyDown for keyboard interactions (Enter/Space)
            tabIndex={0} // Make sure this switch is focusable with Tab
            aria-label="Transaction Frequency"
          />
        }
        label="Transaction Frequency"
      />
    </div>
  );
}

export default SwitchButtons;
