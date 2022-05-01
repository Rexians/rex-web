import { useState } from "react";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import "../styles/Home.css";

const Home = () => {
  const [sidebarState, setSidebarState] = useState(false);

  return (
    <div className="container">
      <Navbar sidebarState={sidebarState} setSidebarState={setSidebarState} />
      {sidebarState && <Sidebar setSidebarState={setSidebarState} />}
    </div>
  );
};

export default Home;
