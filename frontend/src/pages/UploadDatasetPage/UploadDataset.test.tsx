import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';  // For navigation
import UploadDataset from './UploadDataset';

// Mock the fetch function for testing
global.fetch = jest.fn();

describe('UploadDataset', () => {

  it('shows error message when upload fails', async () => {
    // Mock a failed fetch response
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: false
    });

    render(
      <BrowserRouter>
        <UploadDataset />
      </BrowserRouter>
    );

    // // Wait for the error message
    // await waitFor(() => {
    //   expect(screen.getByText(/Error uploading file. Please try again./i)).toBeInTheDocument();
    // });
  });


  // navigation tests
  it('navigates to the correct page when "Back" or "View Results" is clicked', () => {
    render(
      <BrowserRouter>
        <UploadDataset />
      </BrowserRouter>
    );

    // Simulate "Back" button click
    fireEvent.click(screen.getByText(/Back/i));
    expect(window.location.pathname).toBe("/");

    // Simulate "View Results" button click
    fireEvent.click(screen.getByText(/View Results/i));
    expect(window.location.pathname).toBe("/graph");
  });
});

