import { Button } from "@mui/material";
import { ExportService } from "../../../services/ExportService";

function ExportGraphButton() {
  function handleExport() {
    const bignumberelements = document.querySelectorAll('[id^="big-number-"]')  //Changed for the list of tags I updated for big number
    const arrayofids= Array.from(bignumberelements).map(element=>element.id)
    // defined the order I want the elements to be in the pdf-> ie first graph, then big number. 
    const graphId = document.getElementById('graph-canvas')?.id;

    if (graphId) arrayofids.unshift(graphId); //this just adds graph to the array
    ExportService.exportGraphToPDF(arrayofids);
  }
    
    // ExportService.exportGraphToPDF("graph-canvas"); // Call the export service
  return (
    <Button
      variant="contained"
      data-testid="forecast-button"
      onClick={handleExport}
      color="success"
    >
      Export Graph
    </Button>
  );

}

export default ExportGraphButton;
