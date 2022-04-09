import Node from "./Node";
import "../../styles/alliancewar/NodeSidebar.css";

const Nodes = ({ expanded }) => {
  return (
    <div className="fullnodecontainer">
      <div className={expanded ? "nodescontainerexpanded" : "nodescontainer"}>
        <Node />
        <Node />
        <Node />
        <Node />
        <Node />
        <Node />
      </div>
    </div>
  );
};

export default Nodes;
