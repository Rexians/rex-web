import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircleDot } from "@fortawesome/free-regular-svg-icons";

const Node = ({ nodeName, nodeInfo }) => {
  return (
    <div className="node">
      <div className="nodeheader">
        <FontAwesomeIcon icon={faCircleDot} className="nodeicon" />
        <hr className="nodedivider"></hr>
        <h3 className="nodename">{nodeName}</h3>
      </div>
      <p className="nodeinfo">{nodeInfo}</p>
    </div>
  );
};

export default Node;
