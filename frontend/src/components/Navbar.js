import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { SocialIcon } from "react-social-icons";
import useLogOut from "../helpers/UseLogout";
import "../styles/Navbar.css";

const Navbar = ({ sidebarState, setSidebarState }) => {
  const [navbarState, setNavbarState] = useState(true);

  // When clicked, open or close sidebar
  const showSidebar = () => setSidebarState(!sidebarState);
  // When clicked, logout user
  const { logoutUser } = useLogOut();

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
      <div className="custom-navbar">
        {window.localStorage.getItem("logged") === "false" ? (
          <Link to="/login" className="auth">
            Login
          </Link>
        ) : (
          <div className="auth" onClick={() => logoutUser()}>
            Logout
          </div>
        )}
        <Link to="/home" className="home-title ">
          R E X I A N S
        </Link>
        <SocialIcon
          network="discord"
          className="discord"
          url="https://discord.gg/eNB9Hq3htd"
          style={{ height: 35, width: 35 }}
        ></SocialIcon>
        <SocialIcon
          network="twitter"
          className="twitter"
          url="https://twitter.com/TheRexians"
          style={{ height: 35, width: 35 }}
        ></SocialIcon>
        <button className="sidebar-button" onClick={showSidebar}>
          &#8801;
        </button>
      </div>
    )
  );
};

export default Navbar;
