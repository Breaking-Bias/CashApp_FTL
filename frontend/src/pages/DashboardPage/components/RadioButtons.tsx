import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";

interface Props {
  mode: string;
  setMode: (newValue: string) => void;
}
// 0 means number of transaction, 1 means value of transaction

function RadioButtons({ mode, setMode }: Props) {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setMode(event.target.value);
  };

  return (
    <RadioGroup
      row // makes the radio buttons inline
      defaultValue="0"
      value={mode}
      onChange={handleChange}
      color="success"
    >
      <FormControlLabel
        value="0"
        control={<Radio />}
        label="Transaction Frequency"
      />
      <FormControlLabel value="1" control={<Radio />} label="Revenue" />
    </RadioGroup>
  );
}

export default RadioButtons;
