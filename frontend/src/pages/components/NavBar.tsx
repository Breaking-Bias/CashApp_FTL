import React, { useState } from "react";
import { NavLink } from "react-router-dom"; // Import NavLink for active link support
import "./NavBar.css";

const Navbar: React.FC = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen((prevState) => !prevState);
  };

  return (
    <header className="header">
      <img
                alt="Logo"
                src="/logo.png"
                style={{ width: "60px", height: "auto", margin: 0 }}
              />
      <p style={{ fontSize: 30, margin: 0 }}>
        <strong>Breaking Bias</strong>
      </p>
      <nav>
        <div className="nav-links">
          {/* Home Link with Dropdown */}
          <div className="dropdown-container">
            <NavLink
              to="/"
              className={({ isActive }) => (isActive ? "active" : "")}
              onClick={toggleDropdown} // Toggle dropdown when "Home" is clicked
            >
              Home
            </NavLink>
            {isDropdownOpen && (
              <div className="dropdown-menu">
                <a href="#Start">Start</a>
                <a href="#welcome">Welcome</a>
                <a href="#mission">Mission</a>
              </div>
            )}
          </div>

          <NavLink
            to="/upload-dataset"
            className={({ isActive }) => (isActive ? "active" : "")} // Apply 'active' class when the link is active
          >
            Upload Dataset
          </NavLink>
          <NavLink
            to="/graph"
            className={({ isActive }) => (isActive ? "active" : "")}
          >
            Dashboard
          </NavLink>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
