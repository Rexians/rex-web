import { useState } from "react";
import "../../styles/alliancewar/TierForm.css";
// WORK ON ADDING TIER SELECTION FORM
const TierForm = ({ warInfo }) => {
  const [tierSelectionState, switchToSelection] = useState(false);

  return (
    <>
      <div className="awinfo">
        <div className="awheader">Alliance War</div>
        <hr className="awdivider"></hr>
        <div className="awstats">
          <div>Tier</div>
          <div className="tier">{warInfo["tier"]}</div>
        </div>
        <div className="awstats">
          <div>Difficulty</div>
          <div className="difficulty">{warInfo["difficulty"]}</div>
        </div>
        <div className="awstats">
          <div>Tier Multiplier</div>
          <div className="tiermult">{warInfo["tier_multiplier"]}</div>
        </div>
        <div className="awstats">
          <div>Tier Rank</div>
          <div className="tierrank">{warInfo["tier_rank"]}</div>
        </div>
        <button className="tierbutton">Change Tier</button>
      </div>
    </>
  );
};

export default TierForm;
