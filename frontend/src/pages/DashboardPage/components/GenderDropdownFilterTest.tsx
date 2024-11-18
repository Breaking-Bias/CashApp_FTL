import { render, screen, fireEvent } from "@testing-library/react";
import GenderDropdownFilter from "./GenderDropdownFilter";

describe("GenderDropdownFilter", () => {
  it("should call onSelectChange with the correct value when an option is selected", () => {
    //Note to reader - this makes a mock of the change. The actual implementation doesn't matter just that it's being used. ie how many times it's been called etc 
    const mockOnSelectChange = jest.fn();
    render(<GenderDropdownFilter onSelectChange={mockOnSelectChange} />);
    // There's like a teting environment created somewhere (idek where) that renders this component externally

    const selectElement = screen.getByLabelText("Gender"); 

    fireEvent.change(selectElement, { target: { value: "Male" } });

    // firevent change simulates a user changing the value (in the gender case its male)

    expect(mockOnSelectChange).toHaveBeenCalledWith("Male");
  });
  // expect is like assert

  it("should render the correct options in the dropdown", () => {
    // Render the component
    render(<GenderDropdownFilter onSelectChange={() => {}} />);

    // Assert: Check if the options are rendered correctly
    const noFilterOption = screen.getByText("No Filter");
    const maleOption = screen.getByText("Male");
    const femaleOption = screen.getByText("Female");
    const nonBinaryOption = screen.getByText("Non-Binary");
    const otherOption = screen.getByText("Other");

    // this is just checking if the options exist in the document

    expect(noFilterOption).toBeInTheDocument();
    expect(maleOption).toBeInTheDocument();
    expect(femaleOption).toBeInTheDocument();
    expect(nonBinaryOption).toBeInTheDocument();
    expect(otherOption).toBeInTheDocument();
  });

  it("should update the selected value when an option is selected", () => {
    const mockOnSelectChange = jest.fn();

    render(<GenderDropdownFilter onSelectChange={mockOnSelectChange} />);

    const selectElement = screen.getByLabelText("Gender");
    fireEvent.change(selectElement, { target: { value: "Female" } });

    expect(selectElement).toHaveValue("Female");
  });
});
