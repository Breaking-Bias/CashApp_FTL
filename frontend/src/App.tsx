import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import UploadDataset from "./pages/UploadDatasetPage/UploadDataset.tsx";
import HomePage from "./pages/HomePage/HomePage";
import DashboardPage from "./pages/DashboardPage/DashboardPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/upload-dataset" element={<UploadDataset />} />
        <Route path="/graph" element={<DashboardPage />} />
      </Routes>
    </Router>
  );
}

export default App;
