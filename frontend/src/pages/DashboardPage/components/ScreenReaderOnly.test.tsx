import { render, screen } from "@testing-library/react";
import GraphDescription from "./ScreenReaderOnly";

describe("ScreenReaderOnly", () => {
  it("Renders the alert properly", () => {
    const modeGraphData = {
      average_difference: 10,
      total_difference: 48,
      past_biased_line: [{ value: 4 }, { value: 10 }],
      predicted_biased_line: [{ value: 4 }, { value: 10 }],
      predicted_unbiased_line: [{ value: 4 }, { value: 10 }],
    };

    render(
      <GraphDescription
        modeGraphData={modeGraphData}
        mode="0"
        filterGender="Male"
        filterRace="NoFilter"
      />
    );

    const alert = screen.getByTestId("test-alert");

    expect(alert).toBeInTheDocument();
  });
});
