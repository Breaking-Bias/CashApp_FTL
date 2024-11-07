import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";

interface Props {
  filterFactor: string;
  setFilterFactor: (newValue: string) => void;
}

function RadioButtons({ filterFactor, setFilterFactor }: Props) {
  const handleChange = (event: any) => {
    setFilterFactor(event.target.value);
  };

  return (
    <RadioGroup
      defaultValue="noFilter"
      value={filterFactor}
      onChange={handleChange}
    >
      <FormControlLabel value="female" control={<Radio />} label="Female" />
      <FormControlLabel value="male" control={<Radio />} label="Male" />
      <FormControlLabel value="other" control={<Radio />} label="Other" />
      <FormControlLabel
        value="noFilter"
        control={<Radio />}
        label="No Filter"
      />
    </RadioGroup>
  );
}

export default RadioButtons;
