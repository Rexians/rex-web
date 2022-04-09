import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircleDot } from "@fortawesome/free-regular-svg-icons";

const Node = () => {
  return (
    <div className="node">
      <div className="nodeheader">
        <FontAwesomeIcon icon={faCircleDot} className="nodeicon" />
        <hr className="nodedivider"></hr>
        <h3 className="nodename">Aggression Prowess</h3>
      </div>
      <p className="nodeinfo">
        Every 2 seconds the defender gains a prowess buff that increases special
        damage.
      </p>
    </div>
  );
};

export default Node;
