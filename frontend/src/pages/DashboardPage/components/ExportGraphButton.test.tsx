import { render, screen } from "@testing-library/react";
import ExportGraphButton from "./ExportGraphButton";

jest.mock("../../../services/ExportService", () => ({
    ExportService: {
      exportGraphToPDF: jest.fn(),
    },
  }));
  
  beforeAll(() => {
    window.HTMLCanvasElement.prototype.getContext = jest.fn().mockReturnValue({
      fillRect: jest.fn(),
      drawImage: jest.fn(),
      getImageData: jest.fn(),
      putImageData: jest.fn(),
      createLinearGradient: jest.fn(),
      createPattern: jest.fn(),
    });
  });

describe("ExportGraphButton Component", () => {
  it("renders the button with the correct text", () => {
    render(<ExportGraphButton />);

    // Check if the Export Graph button is rendered with the correct text
    const button = screen.getByText("Export Graph");
    expect(button).toBeInTheDocument();
  });

  it("has the correct data-testid", () => {
    render(<ExportGraphButton />);

    // Check if the button has the correct data-testid
    const button = screen.getByTestId("forecast-button");
    expect(button).toBeInTheDocument();
  });
});
