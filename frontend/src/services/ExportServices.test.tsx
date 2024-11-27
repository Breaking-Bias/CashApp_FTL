import { render, screen } from '@testing-library/react';
import { ExportService } from './ExportService';  // Adjust the import path to match your actual file structure
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

// Mock jsPDF and html2canvas
jest.mock('jspdf', () => {
  return jest.fn().mockImplementation(() => ({
    addImage: jest.fn(),
    save: jest.fn(),
  }));
});

jest.mock('html2canvas', () => jest.fn());

// Example component to test the export functionality
const GraphComponent = () => (
  <div id="graph-id">
    <canvas></canvas>
  </div>
);

describe('ExportService', () => {
//   it('should export the graph to a PDF when the element exists', async () => {
    
//     // Render the GraphComponent to the document body
//     render(<GraphComponent />);

//     // Check if the element exists in the document
//     const graphElement = screen.getByTestId('graph-id');
//     expect(graphElement).toBeInTheDocument();

//     // Call the export function
//     ExportService.exportGraphToPDF('graph-id');

//     // Wait for the async code to finish (since html2canvas is async)
//     await Promise.resolve();

//     // Check if jsPDF methods were called
//     const doc = new jsPDF();
//     expect(doc.addImage).toHaveBeenCalledWith('data:image/png;base64,someimage', 'PNG', 10, 10, 180, 160);
//     expect(doc.save).toHaveBeenCalledWith('graph.pdf');
//   });

  it('should alert if the graph element is not found', () => {
    // Mock the alert method
    const alertMock = jest.spyOn(window, 'alert').mockImplementation(() => {});

    // Call export with a non-existent element ID
    ExportService.exportGraphToPDF('non-existent-id');

    // Check if alert was called
    expect(alertMock).toHaveBeenCalledWith('Graph not found!');
  });

//   it('should call html2canvas with the correct element', async () => {
    
//     // Render the GraphComponent to the document body
//     render(<GraphComponent />);

//     // Call export function
//     ExportService.exportGraphToPDF('graph-id');
//     await Promise.resolve();

//     // Check if html2canvas was called with the correct element
//     const graphElement = screen.getByTestId('graph-id');
//     expect(html2canvas).toHaveBeenCalledWith(graphElement);
//   });
});
