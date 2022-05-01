import { Link } from "react-router-dom";
import "../styles/Sidebar.css";

const Sidebar = ({ setSidebarState }) => {
  return (
    <div className="sidebar">
      <Link
        className="sidebaroptions"
        to="/roster"
        onClick={() => setSidebarState(false)}
      >
        Roster
      </Link>
      <Link
        className="sidebaroptions"
        to="/alliance"
        onClick={() => setSidebarState(false)}
      >
        Alliance
      </Link>
      <Link
        className="sidebaroptions"
        to="/war/1"
        onClick={() => setSidebarState(false)}
      >
        Alliance War
      </Link>
      <div className="sidebaroptions">Coming soon...</div>
    </div>
  );
};

export default Sidebar;
