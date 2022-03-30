import "../styles/Sidebar.css";
import { Link } from "react-router-dom";

const Sidebar = ({setSidebarState }) => {

  const showSidebar = () => setSidebarState(false)

  return (
    <div className="sidebar">
      <Link className="sidebaroptions" to="/roster" onClick={showSidebar}>
        Roster
      </Link>
      <Link className="sidebaroptions" to="/alliance" onClick={showSidebar}>
        Alliance
      </Link>
      <Link className="sidebaroptions" to="/war" onClick={showSidebar}>
        Alliance War
      </Link>
      <div className="sidebaroptions">Coming soon...</div>
    </div>
  );
};

export default Sidebar;
