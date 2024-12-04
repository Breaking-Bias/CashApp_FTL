import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import HomePage from "../HomePage/HomePage";

describe("HomePage Component", () => {
  test("renders the logo, heading, subheading, and button", () => {
    render(
      <MemoryRouter>
        <HomePage />
      </MemoryRouter>
    );


    expect(screen.getByText("Cash ML Bias Dashboard")).toBeInTheDocument();
    expect(screen.getByText("Make Better Decisions.")).toBeInTheDocument();

    const button = screen.getByRole("button", { name: "Start" });
    expect(button).toBeInTheDocument();
  });

})

