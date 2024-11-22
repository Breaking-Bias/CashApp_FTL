import React from "react";
import Switch from "@mui/material/Switch";
import FormControlLabel from "@mui/material/FormControlLabel";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";

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
    <Box display="flex" justifyContent={"center"} sx={{p: 4}}>
        <Typography variant="h4" component="h1" sx={{marginRight:2}}>
            Graph Type:
        </Typography>
        <Typography variant="h5" component="h1"
                    sx={{marginRight: "8px", marginTop: "5px"}}>
            Frequency
        </Typography>
        <FormControlLabel
            component="h1"
            control={
                <Switch
                    color=""
                    id="revenue-switch"
                    defaultChecked
                    checked={mode === "1"}
                    onChange={handleChange}
                    onKeyDown={handleKeyDown} // Add onKeyDown for keyboard interactions (Enter/Space)
                    tabIndex={0} // Ensure this is focusable after the first switch
                    aria-label="Switch between revenue graph and frequency graph"
                />
            }
            label=""
        />
        <Typography component="h1" variant="h5" sx={{marginLeft: "-13px", marginTop: "5px"}}>
            Revenue
        </Typography>
    </Box>
    </div>
  );
}

export default SwitchButtons;
