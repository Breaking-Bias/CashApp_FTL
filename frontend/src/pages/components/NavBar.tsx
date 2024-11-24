import React from 'react';
import { NavLink } from 'react-router-dom'; // Import NavLink for active link support
import './Navbar.css'; // Import the corresponding CSS file for styling

const Navbar: React.FC = () => {
  return (
    <header className="header">
      <p><strong>Breaking Bias</strong></p>
      <nav>
        <div className="nav-links">
          {/* Navigation links using NavLink */}
          <NavLink
            to="/"
            className={({ isActive }) => (isActive ? 'active' : '')} // Apply 'active' class when the link is active
          >
            Start
          </NavLink>
          <NavLink
            to="/upload-dataset"
            className={({ isActive }) => (isActive ? 'active' : '')} // Apply 'active' class when the link is active
          >
            Upload Dataset
          </NavLink>
          <NavLink
            to="/graph"
            className={({ isActive }) => (isActive ? 'active' : '')} // Apply 'active' class when the link is active
          >
            Main Page
          </NavLink>

        </div>
      </nav>
    </header>
  );
};

export default Navbar;
