import {useState} from "react";
import {Select, MenuItem, FormControl, InputLabel} from "@mui/material";

interface DropdownFilterProps {
  onSelectChange: (value: string) => void; // Function to handle changes in App.tsx
}

function DropdownFilter({ onSelectChange }: DropdownFilterProps) {
  const [selectedOption, setSelectedOption] = useState("");

  const handleChange = (event: { target: { value: any; }; }) => {
    const value = event.target.value;
    setSelectedOption(value);
    onSelectChange(value); // Pass the selected value back to the parent
  };

  
    return (
        <div>
            <FormControl fullWidth>
                <InputLabel>Gender</InputLabel>
                <Select
                    value={selectedOption}
                    onChange={handleChange}
                    label="Gender"
                >
                    <MenuItem value="Male">Male</MenuItem>
                    <MenuItem value="Female">Female</MenuItem>
                </Select>
            </FormControl>

        </div>
    )
}

export default DropdownFilter;
