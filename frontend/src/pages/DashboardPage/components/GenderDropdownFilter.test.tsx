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
});
