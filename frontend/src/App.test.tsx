import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import App from "./App";

test("Renders App", () => {
    render(<App />);
    const title = screen.getByText(/WELCOME TO THE BVPT/i);
    expect(title).toBeInTheDocument();
});
