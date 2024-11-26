import { render, screen } from "@testing-library/react";
import Graph from "./Graph";
import { CYAN, PINK } from "../DashboardPage";
import { DataSeries } from "../../../types";

jest.mock("../DashboardPage", () => ({
  CYAN: "#00FFFF",
  PINK: "#FFC0CB",
}));

// jest.mock('recharts', () => {
//     const OriginalModule = jest.requireActual('recharts')
//     return {
//         ...OriginalModule,
//         ResponsiveContainer: ({ children }) => (
//             <OriginalModule.ResponsiveContainer width={800} height={800}>
//                 {children}
//             </OriginalModule.ResponsiveContainer>
//         ),
//     }
// })

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

    expect(screen.getByTestId("graph-line-1")).toBeInTheDocument();
  });

  //   it("renders the graph with past and predicted data", () => {
  //     render(
  //       <Graph
  //         mode="1"
  //         pastData={mockPastData}
  //         predictedData={mockPredictedData}
  //       />
  //     );

  //     // Check if legends for Biased and Unbiased Data are displayed
  //     expect(screen.getByText("Biased Data")).toBeInTheDocument();
  //     expect(screen.getByText("Unbiased Data")).toBeInTheDocument();

  //     // Check if the X-axis label "Time" is present
  //     expect(screen.getByText("Time")).toBeInTheDocument();

  //     // Check if the Y-axis label is correct based on mode
  //     expect(screen.getByText("Cash Flow ($)")).toBeInTheDocument();
  //   });

  //   it("renders unbiased data line if provided", () => {
  //     const mockPastDataUnbiased: DataSeries = {
  //       name: "Past Unbiased Data",
  //       color: "#00FF00",
  //       data: [
  //         { date: new Date("2023-01-01"), value: 120 },
  //         { date: new Date("2023-02-01"), value: 220 },
  //       ],
  //     };

  //     render(
  //       <Graph
  //         mode="0"
  //         pastData={mockPastData}
  //         pastDataUnbiased={mockPastDataUnbiased}
  //       />
  //     );

  //     // Check if unbiased data is included
  //     expect(screen.getByText("Unbiased Data")).toBeInTheDocument();
  //   });
});
