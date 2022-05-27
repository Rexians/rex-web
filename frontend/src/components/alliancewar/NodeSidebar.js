import { useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircleXmark } from "@fortawesome/free-regular-svg-icons";
import Nodes from "./Nodes";
import "../../styles/alliancewar/NodeSidebar.css";

const NodeSidebar = ({ nodeInfoState, setNodeInfo, tileNumber, nodes }) => {
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
    <div
      className={nodeInfoState["expanded"] ? "expanded-node" : "normal-node"}
    >
      <div>
        <div className="node-title">TILE {tileNumber}</div>
        <FontAwesomeIcon
          className="close-icon"
          icon={faCircleXmark}
          onClick={() => setNodeInfo(false)}
        ></FontAwesomeIcon>
      </div>
      <hr className="divider"></hr>
      <div className="node-title">LOCAL NODE</div>
      <p className="node-info">
        Local Nodes apply a buff to the enemy on this tile.
      </p>
      <Nodes
        expanded={nodeInfoState["expanded"]}
        tileNumber={tileNumber}
        nodes={nodes}
      />
    </div>
  );
};

export default NodeSidebar;
