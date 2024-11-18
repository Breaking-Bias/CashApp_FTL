import { Button } from "@mui/material";
import { ExportService } from "../../../services/ExportService";

function ExportGraphButton() {
  function handleExport() {
    ExportService.exportGraphToPDF("graph-canvas"); // Call the export service
  }
  return (
    <Button
      variant="contained"
      data-testid="forecast-button"
      onClick={handleExport}
      color="success"
    >
      Export Graph to PDF
    </Button>
  );
}

export default ExportGraphButton;
