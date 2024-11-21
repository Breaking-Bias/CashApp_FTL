import React from 'react';
// import './PopUpGuidance.css'; 
// import '.DashboardPage.css';

interface PopUpGuidanceProps {
  isOpen: boolean;
  onClose: () => void;
}

const PopUpGuidance: React.FC<PopUpGuidanceProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="popup-overlay">
     <div className="popup-content">
          <h2>How to Use the App</h2>
          <h3>Working with Graphs</h3>
          <p>Use the button at the top of this page to switch views in:</p>          <ul>
            <p><strong>Transaction Value</strong></p>
            <p><strong>Transaction Frequency</strong></p>
          </ul>
          

          <h3>Customizing Your Graph</h3>
          <ul>
            <p><strong>Filter</strong>: Customize data views using filters.</p>
            <p><strong>Prediction Size</strong>: Adjust the slider to define prediction size.</p>
          </ul>

          <h3>Actions</h3>
          <p>Click <strong>Make Forecast</strong> to visualize data.</p>
          <p>Click <strong>Export Graph</strong> to download a PDF version.</p>
          
          <button className="close-button" onClick={onClose}>Close</button>
        </div>

      </div>

  );
};

export default PopUpGuidance;
