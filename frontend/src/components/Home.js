import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import "../styles/Home.css";

import { useState } from "react";

const Home = () => {
  const [sidebarState, setSidebarState] = useState(false);

  return (
    <div className="container">
      <Navbar sidebarState={sidebarState} setSidebarState={setSidebarState} />
      {sidebarState && <Sidebar />}
    </div>
  );
};

export default Home;
