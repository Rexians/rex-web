import { useEffect, useState } from "react";
import Node from "./Node";
import "../../styles/alliancewar/NodeSidebar.css";

const Nodes = ({ expanded, tileNumber, nodes }) => {
  // Current nodes on tile based on tile number
  const [nodesOnTile, setNodesOnTile] = useState([]);

  // Get nodes for specific tile from all the nodes (nodes)
  const getNodes = async function () {
    var key = 0;
    var nodesOnTile = [];
    for (const [nodeName, nodeInfo] of Object.entries(
      nodes.get(tileNumber.toString())
    )) {
      nodesOnTile.push(
        <Node key={key} nodeName={nodeName} nodeInfo={nodeInfo} />
      );
      key++;
    }
    setNodesOnTile(nodesOnTile);
  };

  useEffect(() => {
    getNodes();
  }, [tileNumber]);

  return (
    <div className="full-node-container">
      <div className={expanded ? "nodes-container-expanded" : "nodes-container"}>
        {nodesOnTile}
      </div>
    </div>
  );
};

export default Nodes;
