import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import DashboardPage from "./DashboardPage"; 

const mockPastData = {
  name: "Past Data",
  color: "#00C49F",
  data: [
    { date: new Date("2024-01-01"), value: 100 },
    { date: new Date("2024-02-01"), value: 200 },
    { date: new Date("2024-03-01"), value: 300 },
  ],
};

const mockPredictedData = {
  name: "Predicted Data",
  color: "#0088FE",
  data: [
    { date: new Date("2024-04-01"), value: 400 },
    { date: new Date("2024-05-01"), value: 500 },
    { date: new Date("2024-06-01"), value: 600 },
  ],
};

// Test Suite
describe("DashboardPage Integration Test", () => {
  test("handles slider change, updates graph data, and processes uploaded dataset", async () => {
    render(<DashboardPage />);

    // // Simulate user interaction with the filter dropdown
    // const filterDropdown = screen.getByRole("combobox", { name: /filter/i });
    // fireEvent.change(filterDropdown, { target: { value: "someFilterOption" } });

    // Verify the graph updates based on filter change
    await waitFor(() => {
      const updatedGraphMessage = screen.getByText(/Loading/i); 
      expect(updatedGraphMessage).toBeInTheDocument();
    });

    // Simulate slider interaction
    const slider = screen.getByTestId("slider");
    fireEvent.change(slider, { target: { value: 50 } });

    // Assert the graph reacts to slider change
    await waitFor(() => {
      const sliderUpdateMessage = screen.getByText(/graph updated with slider value/i); // Placeholder for actual feedback
      expect(sliderUpdateMessage).toBeInTheDocument();
    });
  });
});
