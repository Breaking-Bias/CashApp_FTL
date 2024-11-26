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
    <FormControl fullWidth>
      <InputLabel>Race</InputLabel>
      <Select
        value={selectedOption}
        onChange={handleChange}
        inputProps={{ "data-testid": "race-select" }}
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