import { useEffect } from "react";
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
      {nodeNumber}
    </div>
  );
};

export default NodeSidebar;
