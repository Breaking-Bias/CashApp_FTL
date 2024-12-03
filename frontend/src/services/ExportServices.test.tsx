import { ExportService } from './ExportService';  // Adjust the import path to match your actual file structure

// Mock jsPDF and html2canvas
jest.mock('jspdf', () => {
  return jest.fn().mockImplementation(() => ({
    addImage: jest.fn(),
    save: jest.fn(),
  }));
});

jest.mock('html2canvas', () => jest.fn());

// Example component to test the export functionality

describe('ExportService', () => {

  it('should alert if the graph element is not found', () => {
    // Mock the alert method
    const alertMock = jest.spyOn(window, 'alert').mockImplementation(() => {});

    // Call export with a non-existent element ID
    ExportService.exportGraphToPDF('non-existent-id');

    // Check if alert was called
    expect(alertMock).toHaveBeenCalledWith('Graph not found!');
  });

});
