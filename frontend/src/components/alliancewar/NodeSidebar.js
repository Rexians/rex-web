import { useEffect } from "react";  
import Nodes from "./Nodes";
import "../../styles/alliancewar/NodeSidebar.css";

const NodeSidebar = ({ nodeInfoState, setNodeInfo, nodeNumber }) => {
  // If scroll is more than 4 pixels, expand sidebar to fill removed navbar
  const expand = function () {
    if (window.scrollY > 4) {
      setNodeInfo({ show: true, expanded: true });
    } else {
      setNodeInfo({ show: true, expanded: false });
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", expand);
    return () => {
      window.removeEventListener("scroll", expand);
    };
  }, []);

  return (
    <div className={nodeInfoState["expanded"] ? "expandednode" : "normalnode"}>
      <div className="nodetitle">TILE {nodeNumber}</div>
      <hr className="divider"></hr>
      <div className="nodetitle">LOCAL NODE</div>
      <p className="nodeInfo">
        Local Nodes apply a buff to the enemy on this tile.
      </p>
      <Nodes expanded={nodeInfoState["expanded"]} />
    </div>
  );
};

export default NodeSidebar;
