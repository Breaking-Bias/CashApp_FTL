import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "@/pages/HomePage/HomePage.css";
import Card from '@mui/material/Card';

const HomePage = (): JSX.Element => {
  const navigate = useNavigate();
  const handleUploadDataset = () => {
    navigate("/upload-dataset");
  };

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth"});
  };
  
  return (
    <div>
    <div className="initial-section">
      <img alt="Logo" src="/logo.png" />
      <h1>Cash App</h1>
      <h1>Bias Visualization</h1>
      <br />
      {/* Button to go to Upload Dataset */}
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
        <div className="graph-container">
          {/* Graph on the left */}
          <div className="graph">
            <img alt="Graph Illustration" src="Revenue Gain.png" />
          </div>

          {/* Paragraph on the right */}
          <div className="illustration">
          <p className="goal-text">
            <strong>Goal:</strong>
            <br />
            Provide insights into the potential revenue that could have been earned if specific bias was removed from the dataset. 
            <br />
            <span className="highlighted-text">(represented by the shaded area)</span>
          </p>
          </div>
        </div>
      </div>
  
       {/* Get Started Button */}
       <Button
        className="get-started-button"
        onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
      >
        Go To Top
      </Button>
      </div>
    
  );
};

export default HomePage;