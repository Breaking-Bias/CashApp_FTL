import { Button } from "@mui/material";

interface Props {
  onPress: () => void;
}

function PredictButton({ onPress }: Props) {
  return (
    <Button variant="contained" data-testid="forecast-button" onClick={onPress}>
      Make Forecast
    </Button>
  );
}

export default PredictButton;
