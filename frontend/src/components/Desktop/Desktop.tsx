import { Button } from "@mui/material";
import AppBar from "@mui/material/AppBar";
import image1 from "./image-1.png";
import rectangle2 from "./rectangle-2.svg";
import rectangle3 from "./rectangle-3.svg";
import { useNavigate } from 'react-router-dom';
import "./style.css";

export const Desktop = (): JSX.Element => {
  const navigate = useNavigate();

  const handleLogin = () => {
    navigate('/graph');
  };

  return (
    <AppBar color="default" className="app-bar">
      <div className="overlap-group">
        <img className="image" alt="Logo" src={image1} />
        <div className="div">Cash App</div>
        <div className="text-wrapper">Bias Visualization</div>
        <Button color="success" size="medium" className="login-button" onClick={handleLogin}>
          Login
        </Button>
        <img className="rectangle" alt="Background" src={rectangle2} />
        <img className="img" alt="Decoration" src={rectangle3} />
      </div>
    </AppBar>
  );
};

export default Desktop;