import { Modal, Button } from "react-bootstrap";
import { useState } from "react";
import Select from "react-select";
import { champOptions, tierOptions, rankOptions } from "./Options";
import { addChamp } from "../../api/Roster";
import "../../styles/Roster.css";

const AddChamp = ({ setIsOpen }) => {
  // Added champ/tier/rank state
  const [champ, setChamp] = useState(null);
  const [tier, setTier] = useState(null);
  const [rank, setRank] = useState(null);

  // Valid rank options (changed when tier changes)
  const [validRankOptions, setRankOptions] = useState([]);

  // Check tier and only show valid rank options
  const checkTier = (obj) => {
    var temp;
    if (obj["value"] === 1) {
      temp = rankOptions.slice(0, 2);
    } else if (obj["value"] === 2) {
      temp = rankOptions.slice(0, 3);
    } else if (obj["value"] === 3) {
      temp = rankOptions.slice(0, 4);
    } else if (obj["value"] === 4) {
      temp = rankOptions;
    } else if (obj["value"] === 5) {
      temp = rankOptions;
    } else if (obj["value"] === 6) {
      temp = rankOptions.slice(0, 4);
    }
    setRankOptions(temp);
  };

  // Set champ to selected
  const HandleChampChange = (obj) => {
    setChamp(obj);
  };

  // Set tier to selected. Change rank options based on tier
  const HandleTierChange = (obj) => {
    checkTier(obj);
    setTier(obj);
    setRank(null);
  };

  // Set rank to selected
  const HandleRankChange = (obj) => {
    setRank(obj);
  };

  // TEMPORARAY SAVE - checks if all options are filled
  const Save = () => {
    if (champ === null || rank === null || tier === null) {
      alert("Please fill in all the options");
    } else {
      setIsOpen(false);
    }
    
    addChamp(champ["value"], tier["value"], rank["value"]);
  };

  return (
    <div>
      <Modal.Dialog className="special_modal">
        <Modal.Header>
          <Modal.Title>Add Champion</Modal.Title>
        </Modal.Header>
        <Modal.Body>Champion</Modal.Body>
        <Select
          className="select-option"
          value={champ}
          options={champOptions}
          onChange={(option) => HandleChampChange(option)}
        />
        <Modal.Body>Tier</Modal.Body>
        <Select
          className="select-option"
          value={tier}
          options={tierOptions}
          onChange={(option) => HandleTierChange(option)}
        />
        <Modal.Body>Rank</Modal.Body>
        <Select
          className="select-option"
          value={rank}
          options={validRankOptions}
          onChange={(option) => HandleRankChange(option)}
        />
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setIsOpen(false)}>
            Close
          </Button>
          <Button variant="primary" onClick={Save}>
            Save changes
          </Button>
        </Modal.Footer>
      </Modal.Dialog>
    </div>
  );
};

export default AddChamp;
