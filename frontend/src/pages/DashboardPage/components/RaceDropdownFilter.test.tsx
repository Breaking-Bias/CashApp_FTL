import { render, screen, fireEvent } from "@testing-library/react";
import RaceDropdownFilter from "./RaceDropdownFilter";

describe("RaceDropdownFilter", () => {

  it("should call onSelectChange with the selected value", () => {
    const mockOnSelectChange = jest.fn();
    render(<RaceDropdownFilter onSelectChange={mockOnSelectChange} />);
    
    const select = screen.getByTestId("race-select");
    
    fireEvent.change(select, { target: { value: "Black" } });
    
    expect(mockOnSelectChange).toHaveBeenCalledWith("Black");
    expect(select).toHaveValue("Black");
  });

  it("should call onSelectChange with 'NoFilter' when No Filter is selected", () => {
    const mockOnSelectChange = jest.fn();
    render(<RaceDropdownFilter onSelectChange={mockOnSelectChange} />);

    const select = screen.getByTestId("race-select");
    fireEvent.change(select, { target: { value: "NoFilter" } });

    expect(mockOnSelectChange).toHaveBeenCalledWith("NoFilter");
    expect(select).toHaveValue("NoFilter");
  });

  it("should update the selected value when a different race is selected", () => {
    const mockOnSelectChange = jest.fn();
    render(<RaceDropdownFilter onSelectChange={mockOnSelectChange} />);

    const select = screen.getByTestId("race-select");

    // First select "Black"
    fireEvent.change(select, { target: { value: "Black" } });
    expect(mockOnSelectChange).toHaveBeenCalledWith("Black");
    expect(select).toHaveValue("Black");

    // Then select "White"
    fireEvent.change(select, { target: { value: "White" } });
    expect(mockOnSelectChange).toHaveBeenCalledWith("White");
    expect(select).toHaveValue("White");
  });

  it("should call onSelectChange when a race other than NoFilter is selected", () => {
    const mockOnSelectChange = jest.fn();
    render(<RaceDropdownFilter onSelectChange={mockOnSelectChange} />);

    const select = screen.getByTestId("race-select");

    // Selecting 'Asian' race
    fireEvent.change(select, { target: { value: "Asian" } });

    expect(mockOnSelectChange).toHaveBeenCalledWith("Asian");
    expect(select).toHaveValue("Asian");
  });

  it("should not call onSelectChange if the value doesn't change", () => {
    const mockOnSelectChange = jest.fn();
    render(<RaceDropdownFilter onSelectChange={mockOnSelectChange} />);
    
    const select = screen.getByTestId("race-select");

    // Select the same value twice, on the second change it should not call the handler
    fireEvent.change(select, { target: { value: "Black" } });
    fireEvent.change(select, { target: { value: "Black" } });

    // The handler should be called only once
    expect(mockOnSelectChange).toHaveBeenCalledTimes(1);
  });

  it("should render with an empty string if no option is selected", () => {
    const mockOnSelectChange = jest.fn();
    render(<RaceDropdownFilter onSelectChange={mockOnSelectChange} />);

    const select = screen.getByTestId("race-select");
    expect(select).toHaveValue(""); // Since the initial value is an empty string
  });
});
