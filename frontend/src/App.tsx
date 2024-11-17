import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import UploadDataset from "./pages/UploadDataset";
import HomePage from "./pages/HomePage/HomePage";
import GuidancePage from "./pages/GuidancePage/GuidancePage";
import DashboardPage from "./pages/DashboardPage/DashboardPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/upload-dataset" element={<UploadDataset />} />
        <Route path="/graph" element={<DashboardPage />} />
        <Route path="/guidance" element={<GuidancePage />} />
      </Routes>
    </Router>
  );
}

export default App;
