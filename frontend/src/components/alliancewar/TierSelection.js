import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "../../styles/alliancewar/TierForm.css";

const TierSelection = ({ switchTo }) => {
  const [buttons, changeButtons] = useState([]);

  // Adds 22 buttons corresponding to each tier
  const addButtons = function () {
    var allButtons = [];
    var rowButtons = [];
    for (let i = 1; i < 23; i++) {
      rowButtons.push(
        <Link key={i} to={`/war/${i}`}>
          <button
            className="tier-link"
            onClick={() => {
              switchTo(false);
            }}
          >
            {i}
          </button>
        </Link>
      );
      if (i % 4 === 0) {
        allButtons.push(rowButtons);
        rowButtons = [];
      }
      if (i === 22) {
        rowButtons.push(
          <button
            key={"close"}
            className="close"
            onClick={() => {
              switchTo(false);
            }}
          >
            Close
          </button>
        );
        allButtons.push(rowButtons);
      }
      changeButtons(allButtons);
    }
  };

  useEffect(() => {
    addButtons();
  }, []);

  return (
    <div className="tier-selection">
      <div className="aw-header">Tier Selection</div>
      <hr className="selection-divider"></hr>
      <div className="buttons-container">{buttons[0]}</div>
      <div className="buttons-container">{buttons[1]}</div>
      <div className="buttons-container">{buttons[2]}</div>
      <div className="buttons-container">{buttons[3]}</div>
      <div className="buttons-container">{buttons[4]}</div>
      <div className="buttons-container">{buttons[5]}</div>
      <hr className="selection-divider"></hr>
    </div>
  );
};

export default TierSelection;
