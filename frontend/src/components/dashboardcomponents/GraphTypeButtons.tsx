import React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import {ToggleButton, ToggleButtonGroup} from "@mui/material";

interface Props {
  mode: string;
  setMode: (newValue: string) => void;
}

function GraphTypeButtons({ mode, setMode }: Props) {
    const handleChange = (
        _event: React.MouseEvent<HTMLElement>,
        newMode: string,
    ) => {
        setMode(newMode);
    };

  return (
    <div>
    <Box display="flex" justifyContent={"center"} sx={{p: 4}}>
        <Typography variant="h4" component="h2" sx={{marginRight:2}}>
            Graph Type:
        </Typography>
        <ToggleButtonGroup
            color="success"
            value={mode}
            exclusive
            onChange={handleChange}
            aria-label="Graph type"
        >
            <ToggleButton value="1">Cash Flow</ToggleButton>
            <ToggleButton value="0">Trans. Volume</ToggleButton>
        </ToggleButtonGroup>
    </Box>
    </div>
  );
}

export default GraphTypeButtons;
