import React, {useState} from "react";
import {NavLink} from "react-router-dom"; // Import NavLink for active link support
import "./NavBar.css"; // Import the corresponding CSS file for styling

const Navbar: React.FC = () => {
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);

    const toggleDropdown = () => {
        setIsDropdownOpen((prevState) => !prevState);
    };

    return (
        <header className="header">
            <div style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                width: "100%"
            }}>
                <div style={{display: "flex", alignItems: "center"}}>
                    <img src="/logo.png" alt="Cash app logo"
                         style={{transform: "scale(0.75)"}}/>
                    <p style={{fontSize: 30, margin: 0, paddingLeft: 10}}>
                        <strong>Cash Bias Dashboard</strong>
                    </p>
                </div>
                <nav>
                    <div className="nav-links">
                        {/* Home Link with Dropdown */}
                        <div className="dropdown-container">
                            <NavLink
                                to="/"
                                className={({isActive}) => (isActive ? "active" : "")}
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
                            className={({isActive}) => (isActive ? "active" : "")} // Apply 'active' class when the link is active
                        >
                            Upload Dataset
                        </NavLink>
                        <NavLink
                            to="/graph"
                            className={({isActive}) => (isActive ? "active" : "")}
                        >
                            Dashboard
                        </NavLink>
                    </div>
                </nav>
            </div>
        </header>
);
};

export default Navbar;
