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
    <FormControl fullWidth>
      <InputLabel>Gender</InputLabel>
      <Select
        value={selectedOption}
        onChange={handleChange}
        inputProps={{ "data-testid": "gender-select" }}
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
