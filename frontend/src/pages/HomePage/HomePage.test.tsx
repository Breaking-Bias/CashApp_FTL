import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import HomePage from "./HomePage";

test("Renders CashApp Title", () => {
  console.log("STARTS HERE");
  console.log(process.cwd());
  render(<HomePage />);
  const title = screen.getByText(/Cash App/i);
  expect(title).toBeInTheDocument();
});
