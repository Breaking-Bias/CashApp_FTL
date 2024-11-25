import {useState} from "react";
import {
    Select,
    MenuItem,
    FormControl,
    InputLabel,
    SelectChangeEvent
} from "@mui/material";

interface DropdownFilterProps {
    onSelectChange: (value: string) => void;
}

function GenderDropdownFilter({onSelectChange}: DropdownFilterProps) {
    const [selectedOption, setSelectedOption] = useState("");

    const handleChange = (event: SelectChangeEvent<string>) => {
        const value = event.target.value;
        setSelectedOption(value);
        onSelectChange(value);
    };

    return (
            <FormControl variant="standard" sx={{ m: 1, minWidth: 300 }}>
                <InputLabel sx={{ml: 2}} >Gender</InputLabel>
                <Select
                    value={selectedOption}
                    onChange={handleChange}
                    variant={"filled"}>
                    <MenuItem value="">No Filter</MenuItem>
                    <MenuItem value="Male">Male</MenuItem>
                    <MenuItem value="Female">Female</MenuItem>
                    <MenuItem value="Non-Binary">Non-Binary</MenuItem>
                    <MenuItem value="Other">Other</MenuItem>
                </Select>
            </FormControl>
    );
}

export default GenderDropdownFilter;
