import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import "./UploadDataset.css"
import { Card } from '@mui/material';

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
    <div className="main-class">
      <h1 className="upload-dataset" style={{textAlign:"center", color: "#333",}}>Upload Dataset</h1>
      

      
      <Card className="border-control"  sx={{width:"500px", padding:"40px", maxWidth:"100%", margin:"0 auto" ,border: "2px solid black", boxShadow: 3,}}>
        <h2 className="text-xl font-semibold mb-3">Upload dataset here:</h2>
        
        <div className="flex flex-col items-center gap-6 mb-8">
          <input 
            type="file"
            onChange={handleFileChange}
            className="w-full max-w-md p-2 border rounded"
          />
          <button 
            onClick={handleUpload}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Upload Dataset
          </button>
        </div>
        
        <div className="flex justify-between gap-4">
          <button 
            onClick={() => navigate("/")}
            className="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300"
          >
            Back
          </button>
          <button 
            onClick={() => navigate("/graph")}
            className="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300"
          >
            View Results
          </button>
        </div>
        
        <p className={`mt-4 text-center ${
          message.includes("successfully") ? "text-green-600" : "text-red-600"
        }`}>
          {message}
        </p>
      </Card>
    </div>
  );
};

export default UploadDataset;