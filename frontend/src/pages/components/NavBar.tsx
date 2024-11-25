import React, {useState} from 'react';
import { NavLink } from 'react-router-dom'; // Import NavLink for active link support
import './NavBar.css'; // Import the corresponding CSS file for styling

const Navbar: React.FC = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(prevState => !prevState);
  };


  return (
    <header className="header">
      <p><strong>Breaking Bias</strong></p>
      <nav>
        <div className="nav-links">
          {/* Home Link with Dropdown */}
          <div className="dropdown-container">
            <NavLink
              to="/"
              className={({ isActive }) => (isActive ? 'active' : '')}
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
            className={({ isActive }) => (isActive ? 'active' : '')} // Apply 'active' class when the link is active
          >
            Upload Dataset
          </NavLink>
          <NavLink
            to="/graph"
            className={({ isActive }) => (isActive ? 'active' : '')} 
          >
            Main Page
          </NavLink>

        </div>
      </nav>
    </header>
  );
};

export default Navbar;
