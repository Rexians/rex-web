import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import "../styles/Home.css";

const Home = ({ sidebarState, setSidebarState }) => {
  return (
    <div className="container">
      <Navbar sidebarState={sidebarState} setSidebarState={setSidebarState} />
      {sidebarState && <Sidebar setSidebarState={setSidebarState} />}
    </div>
  );
};

export default Home;
