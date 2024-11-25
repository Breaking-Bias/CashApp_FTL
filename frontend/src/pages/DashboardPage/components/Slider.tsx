import SliderMUI from "@mui/material/Slider";
import {Tooltip} from "@mui/material";

const MIN_SLIDER_VAL = 10;
const MAX_SLIDER_VAL = 100;
export const DEFAULT_SLIDER_VAL = 30;

interface Props {
    sliderValue: number;
    setSliderValue: (newValue: number) => void;
}

function Slider({sliderValue, setSliderValue}: Props) {
    function handleChange(
        _event: Event,
        value: number | number[] | null,
        _activeThumb: number
    ) {
        setSliderValue(value as number);
    }

    return (
        <Tooltip title={
            <span style={{ fontSize: "14px" }}>
            Adjust the prediction size, in number of days.
            </span>}
                 enterDelay={500}
                 leaveDelay={200}>
            <SliderMUI
                data-testid="forecast-slider"
                min={MIN_SLIDER_VAL}
                max={MAX_SLIDER_VAL}
                aria-label="Default"
                valueLabelDisplay="auto"
                value={sliderValue}
                onChange={handleChange}
                color="success"
            />
        </Tooltip>
    );
}

export default Slider;
