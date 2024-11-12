import { Button } from "@mui/material";
import logo from "./logo.png";
// import greenBlob from "./greenBlob.svg";
import { useNavigate } from "react-router-dom";
import "./style.css";

export const Desktop = (): JSX.Element => {
  const navigate = useNavigate();

  const handleUploadDataset = () => {
    navigate("/upload-dataset"); // Route to upload dataset page
  };

  const handleLogin = () => {
    navigate("/graph");
  };
  return (
    <div className="container">
      <img alt="Logo" src={logo} />
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
      >
        Upload Dataset
      </Button>
      <br />
      {/* Button to go to the graph page */}
      <Button
        color="success"
        variant="contained"
        size="large"
        className="login-button"
        onClick={handleLogin}
      >
        Start
      </Button>
    </div>
  );
};

export default Desktop;
