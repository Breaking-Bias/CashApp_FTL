import { useState } from "react";
import {
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  SelectChangeEvent,
} from "@mui/material";

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
    <FormControl variant="standard" sx={{ m: 1, minWidth: 300 }}>
      <InputLabel aria-label="ethnicity to analyse" sx={{ ml: 2 }}>
        Ethnicity
      </InputLabel>
      <Select
        value={selectedOption}
        onChange={handleChange}
        variant={"filled"}
        inputProps={{ "data-testid": "race-select" }}
      >
        <MenuItem value="NoFilter">No Ethnicity Filter</MenuItem>
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
