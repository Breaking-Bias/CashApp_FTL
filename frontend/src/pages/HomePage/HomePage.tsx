import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "@/pages/HomePage/HomePage.css";
import Card from '@mui/material/Card';

const HomePage = (): JSX.Element => {
  const navigate = useNavigate();
  const handleUploadDataset = () => {
    navigate("/upload-dataset");
  };

  return (
    <div className="container">
      <Card className="w-full max-w-md p-6" sx={{width:"500px", padding:"40px", maxWidth:"100%", margin:"0 auto" ,border: "2px solid black", boxShadow: 3,}}>
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
        Start
      </Button>
      </Card>
    </div>
  );
};

export default HomePage;