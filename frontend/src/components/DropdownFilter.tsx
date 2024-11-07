import { useState } from "react";
import { Select, MenuItem, FormControl, InputLabel } from "@mui/material";

interface DropdownFilterProps {
  onSelectChange: (value: string) => void;
}

function DropdownFilter({ onSelectChange }: DropdownFilterProps) {
  const [selectedOption, setSelectedOption] = useState("");

  const handleChange = (event: { target: { value: any; }; }) => {
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
      >
        <MenuItem value="male">Male</MenuItem>
        <MenuItem value="female">Female</MenuItem>
      </Select>
    </FormControl>
  );
}

export default DropdownFilter;
