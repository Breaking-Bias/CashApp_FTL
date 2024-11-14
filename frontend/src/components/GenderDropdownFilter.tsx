import { useState } from "react";
import { Select, MenuItem, FormControl, InputLabel, SelectChangeEvent } from "@mui/material";

interface DropdownFilterProps {
  onSelectChange: (value: string) => void;
}

function GenderDropdownFilter({ onSelectChange }: DropdownFilterProps) {
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
        htmlFor="gender-select"
        sx={{
          // Apply color changes to the label
          transform: selectedOption ? "translate(0, -1.5px) scale(0.75)" : "", // Shrink and move label when selected
          backgroundColor: selectedOption ? "#ffeb3b" : "#f1f1f1", // Yellow background when selected
          paddingInline: "8px", // Padding around label
          borderRadius: "4px", // Rounded corners for the box
          border: selectedOption ? "1px solid #f57c00" : "1px solid #ccc", // Brown border when selected
          color: selectedOption ? "#fff" : "rgba(0, 0, 0, 0.54)", // White text when selected, gray text when unselected
          zIndex: 1, // Ensure label is above the select options
          position: "absolute", // Position the label absolutely within FormControl
          top: 8, // Align label within the select area
          background: selectedOption ? "linear-gradient(to right, #ffeb3b, #fbc02d)" : "none", // Yellow to orange gradient
        }}
      >
        Gender
      </InputLabel>

      {/* The select component */}
      <Select
        id="gender-select"
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
          border: selectedOption ? "1px solid #f57c00" : "1px solid #ccc", // Brown border when selected
          borderRadius: "4px", // Optional: rounded corners to match with the label box
          paddingTop: 2, // Adjust padding to leave space for the label
        }}
      >
        <MenuItem value="NoFilter">No Filter</MenuItem>
        <MenuItem value="Male">Male</MenuItem>
        <MenuItem value="Female">Female</MenuItem>
        <MenuItem value="Non-Binary">Non-Binary</MenuItem>
        <MenuItem value="Other">Other</MenuItem>
      </Select>
    </FormControl>
  );
}

export default GenderDropdownFilter;
