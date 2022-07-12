import { Link } from "react-router-dom";
import "../styles/Sidebar.css";

const Sidebar = ({ setSidebarState }) => {
  return (
    <div className="custom-sidebar">
      <Link
        className="sidebar-options"
        to="/roster"
        onClick={() => setSidebarState(false)}
      >
        Roster
      </Link>
      <Link
        className="sidebar-options"
        to="/alliance"
        onClick={() => setSidebarState(false)}
      >
        Alliance
      </Link>
      <Link
        className="sidebar-options"
        to="/war/1"
        onClick={() => setSidebarState(false)}
      >
        Alliance War
      </Link>
      <div className="sidebar-options">Coming soon...</div>
    </div>
  );
};

export default Sidebar;
