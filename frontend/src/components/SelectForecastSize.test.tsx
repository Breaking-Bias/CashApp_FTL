import { render, screen } from "@testing-library/react";
import SelectForecastSize from "./SelectForecastSize";
import "@testing-library/jest-dom";
import dotenv from "dotenv";

dotenv.config();

test("renders slider and button", () => {
  const mockSetPredictedData = jest.fn();
  render(<SelectForecastSize setPredictedData={mockSetPredictedData} />);

  // Check if the slider is in the document
  const sliderElement = screen.getByTitle("slider-container").children[0];
  expect(sliderElement).toBeInTheDocument();
});
