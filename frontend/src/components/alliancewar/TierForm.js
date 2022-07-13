import { useState } from "react";
import TierSelection from "./TierSelection";
import "../../styles/alliancewar/TierForm.css";

const TierForm = ({ warInfo }) => {
  const [tierSelectionState, switchToSelection] = useState(false);

  if (tierSelectionState) {
    return <TierSelection switchTo={switchToSelection} />;
  } else {
    return (
      <>
        <div className="aw-info">
          <div className="aw-header">Alliance War</div>
          <div>
            <hr className="aw-divider"></hr>
          </div>
          <div className="aw-stats">
            <div>Tier</div>
            <div className="tier">{warInfo["tier"]}</div>
          </div>
          <div className="aw-stats">
            <div>Difficulty</div>
            <div className="difficulty">{warInfo["difficulty"]}</div>
          </div>
          <div className="aw-stats">
            <div>Tier Multiplier</div>
            <div className="tiermult">{warInfo["tier_multiplier"]}</div>
          </div>
          <div className="aw-stats">
            <div>Tier Rank</div>
            <div className="tierrank">{warInfo["tier_rank"]}</div>
          </div>
          <button
            className="tier-button"
            onClick={() => {
              switchToSelection(true);
            }}
          >
            Change Tier
          </button>
        </div>
      </>
    );
  }
};

export default TierForm;
