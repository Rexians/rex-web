import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import { useState } from "react";

const Navigation = () => {
  const [sidebarState, setSidebarState] = useState(false);
  return (
    <div>
      <Navbar sidebarState={sidebarState} setSidebarState={setSidebarState} />
      {sidebarState && <Sidebar setSidebarState={setSidebarState} />}
    </div>
  );
};

export default Navigation;
