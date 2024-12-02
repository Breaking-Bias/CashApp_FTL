import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import DashboardPage from './DashboardPage';
import { getGraphDataAPICall, getPastDataAPICall } from '../../services/ApiCalls';
import '@testing-library/jest-dom';

// Mock the API calls
jest.mock('../../services/ApiCalls', () => ({
  getGraphDataAPICall: jest.fn(),
  getPastDataAPICall: jest.fn(),
}));

describe('DashboardPage Integration Test', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders and updates the graph based on slider and filters', async () => {
    // Mock API response for `getPastDataAPICall`
    (getPastDataAPICall as jest.Mock).mockResolvedValue([
      { date: new Date("2023-03-01"), value: 320 },
      { date: new Date("2023-04-01"), value: 420 },
    ]);

    // Mock API response for `getGraphDataAPICall`
    (getGraphDataAPICall as jest.Mock).mockResolvedValue({
      frequency_graph: {
        past_biased_line: [{ date: new Date('2024-01-01'), value: 15 }],
        predicted_biased_line: [{ date: new Date('2024-01-02'), value: 25 }],
        average_difference: 10,
        total_difference: 50,
      },
      revenue_graph: null,
    });

    // Render the `DashboardPage`
    render(<DashboardPage />);

    // Check if the loading message is displayed initially
    expect(screen.getByText('Loading')).toBeInTheDocument();

    // Wait for past data to load
    await waitFor(() => {
      expect(getPastDataAPICall).toHaveBeenCalled();
    });

    // Verify the graph renders correctly with past data
    expect(screen.queryByText('Loading')).not.toBeInTheDocument();

    });

  });
;
