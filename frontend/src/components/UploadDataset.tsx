import React, { useState } from 'react';

interface DataRow {
  [key: string]: string | number;
}

function UploadDataset() {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState<string>("");
  const [previewData, setPreviewData] = useState<DataRow[]>([]);

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
        setMessage("Failed to upload the file. Server returned an error.");
        return;
      }
    
      const result = await response.json();
    
      // Set success message if upload goes through
      setMessage(result.message || "File uploaded successfully!");
    } catch (error) {
      setMessage("Error uploading file. Please try again.");
      console.error("Upload error:", error);
    }
  };

  return (
    <div>
      <h2>Upload Dataset</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload Dataset</button>
      <p>{message}</p>

      {/* Display preview of the data if available */}
      {previewData.length > 0 && (
        <div>
          <h3>Data Preview:</h3>
          <table>
            <thead>
              <tr>
                {Object.keys(previewData[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {previewData.map((row, index) => (
                <tr key={index}>
                  {Object.values(row).map((value, i) => (
                    <td key={i}>{String(value)}</td> // Convert values to strings
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default UploadDataset;
