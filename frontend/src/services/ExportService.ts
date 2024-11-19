import jsPDF from "jspdf";
import html2canvas from "html2canvas";
import "./ExportService.css"

export const ExportService = {
  exportGraphToPDF: (elementId:string) => {
    const doc = new jsPDF();
    const graphElement = document.getElementById(elementId);

    if (graphElement) {
      // Convert the graph component to an image
      html2canvas(graphElement).then((canvas) => {
        const imgData = canvas.toDataURL("image/png");
        
        // Add the image to the PDF
        doc.addImage(imgData, "PNG", 10, 10, 180, 160);
        doc.save("graph.pdf");
      });
    } else {
      alert("Graph not found!");
    }
  },
};