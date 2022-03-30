import "../styles/Navbar.css";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";

const Navbar = ({ sidebarState, setSidebarState }) => {
  const showSidebar = () => setSidebarState(!sidebarState);
  const [navbarState, setNavbarState] = useState(true);

  const controlNavbar = () => {
    if (window.scrollY > 5) {
      setNavbarState(false);
      setSidebarState(false);
    } else {
      setNavbarState(true);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", controlNavbar);
    return () => {
      window.removeEventListener("scroll", controlNavbar);
    };
  }, []);

  return (
    navbarState && (
      <div className="navbar">
        <Link to="/home" className="title">
          R E X I A N S
        </Link>
        <button className="sidebarbutton" onClick={showSidebar}>
          &#8801;
        </button>
      </div>
    )
  );
};

export default Navbar;
