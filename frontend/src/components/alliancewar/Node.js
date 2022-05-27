import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircleDot } from "@fortawesome/free-regular-svg-icons";

const Node = ({ nodeName, nodeInfo }) => {
  return (
    <div className="node">
      <div className="node-header">
        <FontAwesomeIcon icon={faCircleDot} className="node-icon" />
        <hr className="node-divider"></hr>
        <h3 className="node-name">{nodeName}</h3>
      </div>
      <p className="node-description">{nodeInfo}</p>
    </div>
  );
};

export default Node;
