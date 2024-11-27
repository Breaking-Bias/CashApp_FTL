import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import "./UploadDataset.css";
import { Card } from '@mui/material';
import Navbar from '../../components/NavBar.tsx';

function UploadDataset() {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState<string>("");
  const navigate = useNavigate();

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
      setMessage("");  
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('https://breakingbiasbigboss.zapto.org/upload-dataset', {
        method: 'POST',
        body: formData,
      });
      
      if (!response.ok) {
        setMessage("Failed to upload the file. Server returned error.");
        return;
      }
      const result = await response.json();
    
      setMessage(result.message || "File uploaded successfully!");
    } catch (error) {
      setMessage("Error uploading file. Please try again.");
      console.error(error);
    }
  };

  return (
    <div className="main-class">
      <Navbar />
      
      <Card
        className="border-control"
        sx={{
          width: "500px",
          padding: "40px",
          maxWidth: "100%",
          margin: "0 auto",
          border: "2px solid black",
          boxShadow: 3,
        }}
      >
        <h1
          className="upload-dataset"
          style={{ textAlign: "center", color: "#333", marginBottom: "20px" }}
        >
          Upload Dataset
        </h1>
        
        <div className="flex flex-col items-center gap-6 mb-8">
          {/* Label for file input */}
          <label className="sr-only" htmlFor="file-upload">Choose a Dataset to Upload</label>
          <input
            type="file"
            onChange={handleFileChange}
            className="w-full max-w-md p-2 border rounded"
            aria-label="Choose a file to upload"
            aria-describedby="file-upload-description"
          />
          <span id="file-upload-description" className="sr-only">
            Select a file from your device to upload.
          </span>

          <button
            onClick={handleUpload}
            className="upload-button"
            aria-label="Upload Dataset"
          >
            Upload Dataset
          </button>
        </div>
        
        <div className="nav-buttons-container">
          <button
            onClick={() => navigate("/")}
            className="nav-button"
            aria-label="Back to home"
          >
            Back
          </button>
          <button
            onClick={() => navigate("/graph")}
            className="nav-button"
            aria-label="View Results"
          >
            View Results
          </button>
        </div>
        
        <p
          className={`mt-4 text-center ${
            message.includes("successfully") ? "text-green-600" : "text-red-600"
          }`}
        >
          {message}
        </p>
      </Card>
    </div>
  );
}

export default UploadDataset;
