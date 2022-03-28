import "../styles/Navbar.css";
import { Link } from "react-router-dom";

const Navbar = ({ sidebarState, setSidebarState }) => {
  const showSidebar = () => setSidebarState(!sidebarState);

  return (
    <div className="navbar">
      <Link to="/home" className="title">
        R E X I A N S
      </Link>
      <button className="sidebarbutton" onClick={showSidebar}>
        +
      </button>
    </div>
  );
};

export default Navbar;
