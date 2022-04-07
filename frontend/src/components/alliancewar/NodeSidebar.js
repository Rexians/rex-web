import { useState, useEffect } from "react";
import "../../styles/alliancewar/NodeSidebar.css";

const NodeSidebar = ({ nodeNumber }) => {
  // State for sidebar when scrolling
  const [expanded, setExpanded] = useState(false);

  // If scroll is more than 4 pixels, expand sidebar to fill removed navbar
  const expand = function () {
    if (window.scrollY > 4) {
      console.log(window.scrollY);
      setExpanded(true);
    } else {
      setExpanded(false);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", expand);
    return () => {
      window.removeEventListener("scroll", expand);
    };
  }, []);

  return (
    <div className={expanded ? "expandednode" : "normalnode"}>{nodeNumber}</div>
  );
};

export default NodeSidebar;
