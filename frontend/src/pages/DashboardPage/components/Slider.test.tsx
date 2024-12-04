import { render, screen } from "@testing-library/react";
import Slider from "./Slider";

describe("Slider Component", () => {
  const mockSetSliderValue = jest.fn();

  it("renders the slider in the document", () => {
    render(
      <Slider sliderValue={30} setSliderValue={mockSetSliderValue} />
    );

    // Check if the slider is rendered and exists in the document
    const slider = screen.getByTestId("forecast-slider");
    expect(slider).toBeInTheDocument();
  });

  it("calls setSliderValue when the slider is changed", () => {
    render(
      <Slider sliderValue={30} setSliderValue={mockSetSliderValue} />
  );
  })
})
