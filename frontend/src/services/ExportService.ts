import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export const ExportService = {
  exportGraphToPDF: async (
    elementIds: string[], 
    options: {
      filename?: string;
      x?: number;
      y?: number;
      width?: number;
      height?: number;
      imageType?: "PNG" | "JPEG";
      verticalSpacing?: number;
    } = {}
  ) => {

    const {
      filename = "fullexport.pdf",
      x = 10,
      y = 10,
      width = 180,
      height = 80,
      imageType = "PNG",
      verticalSpacing = 90
    } = options;

    const doc = new jsPDF();
    let currentYOffset = y;

    for (const elementId of elementIds ) {
      const graphElement = document.getElementById(elementId)
      
      if (graphElement){
        try{
        const image = (await html2canvas(graphElement));
        const imgData = image.toDataURL("image/${imageType.toLowerCase()}`");
        doc.addImage(imgData, imageType, x, currentYOffset, width, height)
        currentYOffset+=verticalSpacing;
      } catch (error) {
        console.error(`Error exporting element ${elementId}:`, error);
        alert(`Failed to export element: ${elementId}`);
      }


    
    }
  }
  doc.save(filename);
},
};


//   exportGraphToPDF: (elementId:string) => {
    

//     const doc = new jsPDF();
//     const graphElement = document.getElementById(elementId);

//     if (graphElement) {
//       // Convert the graph component to an image
//       html2canvas(graphElement).then((canvas) => {
//         const imgData = canvas.toDataURL("image/png");
        
        
//         // Add the image to the PDF
//         doc.addImage(imgData, "PNG", 10, 10, 180, 160);
//         doc.save("graph.pdf");
//       });
//     } else {
//       alert("Graph not found!");
//     }
//   },
// };