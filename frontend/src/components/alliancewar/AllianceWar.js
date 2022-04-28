import { useParams } from "react-router-dom";
import Navbar from "../Navbar";
import Sidebar from "../Sidebar";
import Board from "./Board";

const AllianceWar = ({ sidebarState, setSidebarState }) => {
  // Gets tier param from URL
  var { tier } = useParams();
  // If URL was /war, make tier 1
  if (tier === undefined) {
    tier = 1;
  }
  return (
    <div>
      <Board tier={tier} />
      <Navbar sidebarState={sidebarState} setSidebarState={setSidebarState} />
      {sidebarState && <Sidebar setSidebarState={setSidebarState} />}
    </div>
  );
};

export default AllianceWar;
