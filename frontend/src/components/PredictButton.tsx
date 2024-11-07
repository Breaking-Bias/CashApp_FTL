import { Button } from "@mui/material";

interface Props {
  predict: () => void;
}

function PredictButton({ predict }: Props) {
  return (
    <Button variant="contained" data-testid="forecast-button" onClick={predict}>
      Make Forecast
    </Button>
  );
}

export default PredictButton;
