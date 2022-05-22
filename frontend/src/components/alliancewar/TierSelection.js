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
            className="tierlink"
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
    <div className="tierselection">
      <div className="awheader">Tier Selection</div>
      <hr className="selectiondivider"></hr>
      <div className="buttonscontainer">{buttons[0]}</div>
      <div className="buttonscontainer">{buttons[1]}</div>
      <div className="buttonscontainer">{buttons[2]}</div>
      <div className="buttonscontainer">{buttons[3]}</div>
      <div className="buttonscontainer">{buttons[4]}</div>
      <div className="buttonscontainer">{buttons[5]}</div>
      <hr className="selectiondivider"></hr>
    </div>
  );
};

export default TierSelection;
