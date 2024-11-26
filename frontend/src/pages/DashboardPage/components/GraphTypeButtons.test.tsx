import { render, screen, fireEvent } from "@testing-library/react";
import GraphTypeButtons from "./GraphTypeButtons";

describe("GraphTypeButtons", () => {
  const mockSetMode = jest.fn();

  it("Renders the graph type buttons properly", () => {
    render(<GraphTypeButtons mode="0" setMode={mockSetMode} />);

    const text = screen.getByText("Graph Type:");

    expect(text).toBeInTheDocument();
  });

  it("Changes state on revenue button click correctly", () => {
    render(<GraphTypeButtons mode="0" setMode={mockSetMode} />);

    const revenueButton = screen.getByTestId("test-revenue-button");

    fireEvent.click(revenueButton);
    expect(mockSetMode).toHaveBeenCalledWith("1");
    
  });

  it("Changes state on frequency button click correctly", () => {
    render(<GraphTypeButtons mode="1" setMode={mockSetMode} />);

    const frequencyButton = screen.getByTestId("test-frequency-button");

    fireEvent.click(frequencyButton);
    expect(mockSetMode).toHaveBeenCalledWith("0");
    
  });
});
