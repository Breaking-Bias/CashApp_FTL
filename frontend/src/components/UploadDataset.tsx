import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";


function UploadDataset() {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState<string>("");
  const navigate = useNavigate();

  // Handle file selection
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
      setMessage(""); // Clear previous message
    }
  };

  // Handle file upload to backend
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
      
      // Check if the response is successful
      if (!response.ok) {
        setMessage("Failed to upload the file. Server returned error.");
        return;
      }
    
      const result = await response.json();
    
      // Update UI with a success or error message only
      setMessage(result.message || "File uploaded successfully!");
    } catch (error) {
      setMessage("Error uploading file. Please try again.");
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Upload Dataset</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload Dataset</button>
      <button onClick={() => navigate("/")}>Go to Home Page</button>
      <button onClick={() => navigate("/graph")}>Go to Main Page</button>
      <p>{message}</p>
    </div>
  );
}

export default UploadDataset;
