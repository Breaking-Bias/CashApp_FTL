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
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <div className="home-page">
      {/* Header Section */}
      <header className="header">
        <p><strong> Breaking Bias</strong></p>
        <div>
          <a href="#Start">Start</a>
          <a href="#welcome">Welcome</a>
          <a href="#mission">Mission</a>
        </div>
      </header>

      {/* Button to go to Upload Dataset */}
      
        <div className="container">
          <section id="Start">
          <Card
            className="w-full max-w-md p-6"
            sx={{ width: "500px", marginTop: "100px", padding: "40px", maxWidth: "100%", margin: "0 auto", border: "2px solid black", boxShadow: 3 }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '10px', justifyContent: 'center' }}>
              <img
                alt="Logo"
                src="/breakingbiaslogo.png"
                className="logo"
                style={{ width: '60px', height: 'auto', margin: 0 }}
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
        </div>
      

      {/* Welcome Section */}
      <section id="welcome">
        <h1 className="text-4xl font-bold mb-4">Welcome to Breaking Bias</h1>
        <p className="text-xl mb-6">Empowering data-driven decisions by identifying and removing biases in your datasets.</p>
      </section>

      {/* How It Works Section */}
      <section id="mission" className="mission-section">
  <div className="mission-content">
    {/* Left Side: Mission and Text */}
    <div className="mission-text">
      <h2 className="mission-heading">Mission</h2>
      <p className="goal-text">
        Provide insights into the potential revenue that could have been earned if specific bias was removed from the dataset.
      </p>
      <p className="highlighted-text">(represented by the shaded area)</p>
    </div>

    {/* Right Side: Graph */}
    <div className="mission-graph">
      <img src="Revenue Gain.png" alt="Graph Illustration" />
    </div>
  </div>
</section>

        {/* Footer Section */}
        <footer className="py-6 bg-green-600 text-white text-center">
          <div className="flex justify-center space-x-8 mb-4"></div>
          <p>© 2024 Breaking Bias | For more information, please contact: <a href="mailto:MrBigBoss@gmail.com" className="hover:underline">MrBigBoss@gmail.com</a></p>
        </footer>

      {/* Scroll to Top Button */}
      <Button
        className="top"
        onClick={scrollToTop}
        sx={{ position: "fixed", bottom: "20px", right: "20px", backgroundColor: "green", color: "white" }}
      >
        Go To Top ↑
      </Button>
    </div>
  );
};

export default HomePage;
