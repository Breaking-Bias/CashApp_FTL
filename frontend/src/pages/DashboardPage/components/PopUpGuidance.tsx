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
        <p>Use "FILTERS" and "PREDICTION SIZE" to customize your data view.</p>
        <p>Click on "MAKE FORECAST" to visualize your data.</p>
        <p></p>
        <button className="close-button" onClick={onClose}>
          Close
        </button>
      </div>
    </div>
  );
};

export default PopUpGuidance;
