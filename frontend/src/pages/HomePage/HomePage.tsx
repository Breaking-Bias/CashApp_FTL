import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "@/pages/HomePage/HomePage.css";

const HomePage = (): JSX.Element => {
  const navigate = useNavigate();

  const handleUploadDataset = () => {
    navigate("/upload-dataset"); // Route to upload dataset page
  };
  
  return (
    <div className="container">
      <img alt="Logo" src="/logo.png" style={{ width: '53px', height: '53px' }} />
      <h1>Cash App</h1>
      <h1>Bias Visualization</h1>
      {/* <img className="rectangle" alt="Background" src={greenBlob} /> */}
      <br />
      {/* Button to go to Upload Dataset */}
      <Button
        color="success"
        variant="contained"
        size="large"
        className="login-button"
        onClick={handleUploadDataset}
        sx={{ marginBottom: 2 }}
      >
        Upload Dataset
      </Button>
      <br />
      {/* Button to go to the graph page */}
    </div>
  );
};

export default HomePage;
