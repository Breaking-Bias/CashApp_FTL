import React from 'react';
// import './PopUpGuidance.css'; 

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
        <p>Navigate through the menu to access different features.</p>
        <p>In this page:</p> 
        <p>Graph could be shown in either <strong>Transaction Value</strong> or <strong>Transaction Frequency</strong> by navigating the button on the top of this page.</p>
        <p>Use <strong>Filter</strong> and <strong>Prediction Size</strong> to customize your data view.</p>
        <p>Click on <strong>Make Forecast</strong> to visualize your data.</p>
        <p>Click on <strong>Export Graph</strong> to get the pdf version.</p>
        <p></p>
        <button className="close-button" onClick={onClose}>
          Close
        </button>
      </div>
    </div>
  );
};

export default PopUpGuidance;
