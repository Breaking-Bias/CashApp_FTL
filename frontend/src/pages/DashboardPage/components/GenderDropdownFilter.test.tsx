import { render, screen, fireEvent } from "@testing-library/react";
import GenderDropdownFilter from "./GenderDropdownFilter";

describe("GenderDropdownFilter", () => {
  it("calls onSelectChange when a gender option is selected", () => {
    const mockOnSelectChange = jest.fn();
    render(<GenderDropdownFilter onSelectChange={mockOnSelectChange} />);

    const select = screen.getByTestId("gender-select");
    fireEvent.change(select, { target: { value: "Male" } });

    expect(mockOnSelectChange).toHaveBeenCalledWith("Male");
    expect(select).toHaveValue("Male");
  });
  
  it("does not call onSelectChange if the value doesn't change", () => {
    const mockOnSelectChange = jest.fn();
    render(<GenderDropdownFilter onSelectChange={mockOnSelectChange} />);
  
    const select = screen.getByTestId("gender-select");
  
    // Simulate selecting the same value again
    fireEvent.change(select, { target: { value: "Male" } });
    fireEvent.change(select, { target: { value: "Male" } });
  
    // Expect the callback to have been called only once
    expect(mockOnSelectChange).toHaveBeenCalledTimes(1);
  });
});
