import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import "../styles/Navbar.css";

const Navbar = ({ sidebarState, setSidebarState }) => {
  const [navbarState, setNavbarState] = useState(true);

  // When clicked, open or close sidebar
  const showSidebar = () => setSidebarState(!sidebarState);

  // When scrolled past 4 pixels, don't show navbar and sidebar
  const controlNavbar = () => {
    if (window.scrollY > 4) {
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
