import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import "./UploadDataset.css"

function UploadDataset() {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState<string>("");
  const navigate = useNavigate();

  // Handle file selection
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
      setMessage(""); 
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

      <div className="file-upload-container">
        <input type="file" onChange={handleFileChange} />
        <button className="upload-button" onClick={handleUpload}>Upload Dataset</button>
      </div>

      <div className="nav-buttons-container">
      <button className="nav-button" onClick={() => navigate("/")}>Back</button>
      <button className="nav-button" onClick={() => navigate("/graph")}>View Results</button>
      </div>

      <p className={message.includes("successfully") ?"success" : "error"}>
        {message}
      </p>
    </div>
  );
}

export default UploadDataset;
