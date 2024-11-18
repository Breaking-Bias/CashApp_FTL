import { Button } from "@mui/material";

interface Props {
  onClick: () => void;
}

function PredictButton({ onClick }: Props) {
  return (
    <Button color="success" variant="contained" data-testid="forecast-button" onClick={onClick}>
      Make Forecast
    </Button>
  );
}

export default PredictButton;
