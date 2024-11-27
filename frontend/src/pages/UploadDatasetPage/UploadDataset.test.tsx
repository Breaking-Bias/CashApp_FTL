import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import UploadDataset from "./UploadDataset";

// Typecasting fetch as a Jest mock
global.fetch = jest.fn() as jest.Mock;

describe("UploadDataset - handleUpload", () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it("displays a success message on successful file upload", async () => {
    render(
      <BrowserRouter>
        <UploadDataset />
      </BrowserRouter>
    );

    const fileInput = screen.getByTestId("test-file-input");
    const uploadButton = screen.getByTestId("upload-dataset-button");

    // Simulate file selection
    const testFile = new File(["dummy content"], "test.csv", {
      type: "text/csv",
    });
    fireEvent.change(fileInput, { target: { files: [testFile] } });

    // Mock a successful upload response
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => ({ message: "File uploaded successfully!" }),
    });

    // Trigger upload
    fireEvent.click(uploadButton);

    // Wait for the success message
    await waitFor(() => {
      expect(
        screen.getByText("File uploaded successfully!")
      ).toBeInTheDocument();
    });
  });

  it("displays an error message on server failure", async () => {
    render(
      <BrowserRouter>
        <UploadDataset />
      </BrowserRouter>
    );

    const fileInput = screen.getByTestId("test-file-input");
    const uploadButton = screen.getByTestId("upload-dataset-button");

    // Simulate file selection
    const testFile = new File(["dummy content"], "test.csv", {
      type: "text/csv",
    });
    fireEvent.change(fileInput, { target: { files: [testFile] } });

    // Mock a failed upload response
    (global.fetch as jest.Mock).mockResolvedValueOnce({ ok: false });

    // Trigger upload
    fireEvent.click(uploadButton);

    // Wait for the error message
    await waitFor(() => {
      expect(
        screen.getByText("Failed to upload the file. Server returned error.")
      ).toBeInTheDocument();
    });
  });

  it("displays an error message when no file is selected", async () => {
    render(
      <BrowserRouter>
        <UploadDataset />
      </BrowserRouter>
    );

    const uploadButton = screen.getByTestId("upload-dataset-button");

    // Trigger upload without selecting a file
    fireEvent.click(uploadButton);

    // Wait for the no-file-selected message
    await waitFor(() => {
      expect(
        screen.getByText("Please select a file to upload.")
      ).toBeInTheDocument();
    });
  });
});
