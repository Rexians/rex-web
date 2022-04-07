import { useState } from "react";
import Navbar from "../Navbar";
import Sidebar from "../Sidebar";
import NodeSidebar from "./NodeSidebar";
import Board from "./Board";

const AllianceWar = ({ sidebarState, setSidebarState }) => {
  return (
    <div>
      <Board />
      <Navbar sidebarState={sidebarState} setSidebarState={setSidebarState} />
      {sidebarState && <Sidebar setSidebarState={setSidebarState} />}
    </div>
  );
};

export default AllianceWar;
