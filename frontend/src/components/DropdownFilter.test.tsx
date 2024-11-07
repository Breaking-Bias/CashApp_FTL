import { render, screen } from "@testing-library/react";
import DropdownFilter from "./DropdownFilter";
import "@testing-library/jest-dom";

test("renders DropdownFilter", () => {
    render (<DropdownFilter onSelectChange={() => {}} />);
  
  // Check if the the Filter is in the document
  const dropdownElement = screen.getByText("Gender");
  expect(dropdownElement).toBeInTheDocument();
})

 
  // Check if the Filter is working with the graph
