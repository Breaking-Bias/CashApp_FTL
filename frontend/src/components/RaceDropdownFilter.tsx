import { useState } from "react";
import { Select, MenuItem, FormControl, InputLabel, SelectChangeEvent } from "@mui/material";

interface DropdownFilterProps {
  onSelectChange: (value: string) => void;
}

function RaceDropdownFilter({ onSelectChange }: DropdownFilterProps) {
  const [selectedOption, setSelectedOption] = useState("");

  const handleChange = (event: SelectChangeEvent<string>) => {
    const value = event.target.value;
    setSelectedOption(value);
    onSelectChange(value);
  };

  return (
    <FormControl fullWidth sx={{ position: "relative" }}>
      {/* FormControl has fullWidth and a relative position to contain the label */}

      <InputLabel
        htmlFor="race-select"
        sx={{
          // Apply color changes to the label
          transform: selectedOption ? "translate(0, -1.5px) scale(0.75)" : "", // Shrink and move label when selected
          backgroundColor: selectedOption ? "#fdd835" : "#f1f1f1", // Light Yellow background when selected, gray when unselected
          paddingInline: "8px", // Padding around label
          borderRadius: "4px", // Rounded corners for the box
          border: selectedOption ? "1px solid #f57c00" : "1px solid #ccc", // Orange border when selected
          color: selectedOption ? "#fff" : "rgba(0, 0, 0, 0.54)", // White text when selected, gray text when unselected
          zIndex: 1, // Ensure label is above the select options
          position: "absolute", // Position the label absolutely within FormControl
          top: 8, // Align label within the select area
          // Gradient background for label when selected (Yellow to Orange gradient)
          background: selectedOption
            ? "linear-gradient(to right, #fdd835, #f57c00)"
            : "none", // Apply gradient when selected
        }}
      >
        Race
      </InputLabel>

      {/* The select component */}
      <Select
        id="race-select"
        value={selectedOption}
        onChange={handleChange}
        MenuProps={{
          PaperProps: {
            style: {
              maxHeight: 300, // Optional: control dropdown height
            },
          },
        }}
        sx={{
          // Style the Select input
          paddingInline: "8px", // Matching padding inside the input
          border: selectedOption ? "1px solid #f57c00" : "1px solid #ccc", // Orange border when selected
          borderRadius: "4px", // Optional: rounded corners to match with the label box
          paddingTop: 2, // Adjust padding to leave space for the label
        }}
      >
        <MenuItem value="NoFilter">No Filter</MenuItem>
        <MenuItem value="Black">Black</MenuItem>
        <MenuItem value="White">White</MenuItem>
        <MenuItem value="Asian">Asian</MenuItem>
        <MenuItem value="Hispanic">Hispanic</MenuItem>
        <MenuItem value="Mixed">Mixed</MenuItem>
        <MenuItem value="Other">Other</MenuItem>
      </Select>
    </FormControl>
  );
}

export default RaceDropdownFilter;
