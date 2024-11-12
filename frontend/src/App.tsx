// import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Desktop } from "./components/Desktop/Desktop";
import MainPage from "./components/MainPage";
import UploadDataset from "./components/UploadDataset";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Desktop />} />
        <Route path="/upload-dataset" element={<UploadDataset />} />
        <Route path="/graph" element={<MainPage />} />
      </Routes>
    </Router>
  );
}

export default App;
