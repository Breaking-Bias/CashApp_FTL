import { render, screen } from "@testing-library/react";
import Graph from "./Graph";
import { CYAN, PINK } from "../DashboardPage";
import { DataSeries } from "../../../types";

jest.mock("../DashboardPage", () => ({
  CYAN: "#00FFFF",
  PINK: "#FFC0CB",
}));

describe("Graph Component", () => {
  const mockPastData: DataSeries = {
    name: "Past Data",
    color: CYAN,
    data: [
      { date: new Date("2023-01-01"), value: 100 },
      { date: new Date("2023-02-01"), value: 200 },
    ],
  };

  const mockPastDataUnbiased: DataSeries = {
    name: "Past Data Unbiased",
    color: CYAN,
    data: [
      { date: new Date("2023-01-01"), value: 120 },
      { date: new Date("2023-02-01"), value: 220 },
    ],
  };

  const mockPredictedData: DataSeries = {
    name: "Predicted Data",
    color: PINK,
    data: [
      { date: new Date("2023-03-01"), value: 300 },
      { date: new Date("2023-04-01"), value: 400 },
    ],
  };

  const mockPredictedDataUnbiased: DataSeries = {
    name: "Predicted Data Unbiased",
    color: PINK,
    data: [
      { date: new Date("2023-03-01"), value: 320 },
      { date: new Date("2023-04-01"), value: 420 },
    ],
  };

  it("Renders the graph when all data is defined", () => {
    render(
      <Graph
        mode="0"
        pastData={mockPastData}
        predictedData={mockPredictedData}
        pastDataUnbiased={mockPastDataUnbiased}
        predictedDataUnbiased={mockPredictedDataUnbiased}
      />
    );

    expect(screen.getByTestId("graph-canvas")).toBeInTheDocument();
  });

  it("Renders the loading state when pastData is undefined", () => {
    render(<Graph mode="1" pastData={undefined} />);

    expect(screen.getByTestId("loading-test-id")).toBeInTheDocument();
  });

  it("Renders legend and axes", () => {
    render(
      <Graph
        mode="1"
        pastData={mockPastData}
        predictedData={mockPredictedData}
        pastDataUnbiased={mockPastDataUnbiased}
        predictedDataUnbiased={mockPredictedDataUnbiased}
      />
    );

    // Check if legends for Biased and Unbiased Data are displayed
    expect(screen.getByText("Biased Data")).toBeInTheDocument();
    expect(screen.getByText("Unbiased Data")).toBeInTheDocument();

    // Check if the X-axis label "Time" is present
    expect(screen.getByText("Date (Months)")).toBeInTheDocument();

    // Check if the Y-axis label is correct based on mode
    expect(screen.getByText("Cash Flow ($)")).toBeInTheDocument();
  });
});
