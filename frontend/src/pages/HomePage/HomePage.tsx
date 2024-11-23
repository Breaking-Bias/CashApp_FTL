import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "@/pages/HomePage/HomePage.css";

const HomePage = (): JSX.Element => {
  const navigate = useNavigate();

  const handleUploadDataset = () => {
    navigate("/upload-dataset"); // Route to upload dataset page
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
    <div>
    
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
