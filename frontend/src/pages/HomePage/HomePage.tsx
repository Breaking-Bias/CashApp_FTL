import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "@/pages/HomePage/HomePage.css";
import Card from "@mui/material/Card";
import Navbar from "../components/NavBar";

const HomePage = (): JSX.Element => {
  const navigate = useNavigate();
  const handleUploadDataset = () => {
    navigate("/upload-dataset");
  };

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <div className="home-page">
      <header>
        <Navbar />
      </header>

      {/* Button to go to Upload Dataset */}

      <div className="container">
        <section id="Start">
          <Card
            className="p-6 w-full max-w-md"
            sx={{
              width: "500px",
              marginTop: "100px",
              padding: "40px",
              maxWidth: "100%",
              margin: "0 auto",
              border: "2px solid black",
              boxShadow: 3,
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "10px",
                marginBottom: "10px",
                justifyContent: "center",
              }}
            >
              <img
                alt="Logo"
                src="/breakingbiaslogo.png"
                className="logo"
                style={{ width: "60px", height: "auto", margin: 0 }}
              />
              <h1>Breaking Bias</h1>
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
        </section>
        <strong style={{ marginTop: 100, fontSize: 30 }} aria-disabled>
          ↓
        </strong>
      </div>

      <section id="welcome">
        <h1 className="mb-4 font-bold text-4xl">Welcome to the BVPT</h1>
        <p className="mb-6 text-xl">
          Your one and only Bias Visualisation and Prediction Tool .
        </p>
      </section>

      <section id="mission" className="mission-section">
        <div className="mission-content">
          <div className="mission-text">
            <h2 className="mission-heading">Mission</h2>
            <p className="goal-text">
              Our tool provides insights into the potential revenue change if
              specific bias was removed from the dataset.
            </p>
            <p className="highlighted-text">(represented by the shaded area)</p>
          </div>

          <div className="mission-graph">
            <img src="Revenue Gain.png" alt="Graph Illustration" />
          </div>
        </div>
      </section>

      {/* Footer Section */}
      <footer className="bg-green-600 py-6 text-center text-white">
        <div className="flex justify-center space-x-8 mb-4"></div>
        <p>© 2024 Breaking Bias</p>
      </footer>

      {/* Scroll to Top Button */}
      <Button
        className="top"
        onClick={scrollToTop}
        sx={{
          position: "fixed",
          bottom: "20px",
          right: "20px",
          backgroundColor: "green",
          color: "white",
        }}
      >
        Go To Top ↑
      </Button>
    </div>
  );
};

export default HomePage;
