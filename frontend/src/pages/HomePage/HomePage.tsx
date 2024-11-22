import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "@/pages/HomePage/HomePage.css";

const HomePage = (): JSX.Element => {
  const navigate = useNavigate();
  const handleUploadDataset = () => {
    navigate("/upload-dataset");
  };

  return (
    <div className="container">
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '10px', justifyContent: 'center' }}>
        <img 
          alt="Logo" 
          src="/breakingbiaslogo.png" 
          className="logo" 
          style={{ width: '60px', height: 'auto', margin: 0 }}
        />
        <h1 style={{ margin: 0 }}>Breaking Bias</h1>
      </div>
      <h2 className="subheading">Make Better Decisions.</h2>
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
    </div>
  );
};

export default HomePage;