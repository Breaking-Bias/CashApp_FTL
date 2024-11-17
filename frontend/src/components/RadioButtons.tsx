import React from "react";
import Switch from "@mui/material/Switch";
import FormControlLabel from "@mui/material/FormControlLabel";

interface Props {
  mode: string;
  setMode: (newValue: string) => void;
}

function SwitchButtons({ mode, setMode }: Props) {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setMode(event.target.checked ? "1" : "0");
  };

  const handleKeyDown = (event: React.KeyboardEvent) => {
    if (event.key === "Enter" || event.key === " ") {
      setMode(mode === "0" ? "1" : "0");
    }
  };

  return (
    <div>
      <FormControlLabel
        control={
          <Switch
            checked={mode === "0"}
            onChange={handleChange}
            onKeyDown={handleKeyDown}
            aria-label="Transaction Frequency"
          />
        }
        label="Transaction Frequency"
      />
      <FormControlLabel
        control={
          <Switch
            checked={mode === "1"}
            onChange={handleChange}
            onKeyDown={handleKeyDown}
            aria-label="Revenue"
          />
        }
        label="Revenue"
      />
    </div>
  );
}

export default SwitchButtons;
