import { useParams } from "react-router-dom";
import Navigation from "../Navigation";
import Board from "./Board";

const AllianceWar = () => {
  // Gets tier param from URL
  var { tier } = useParams();
  // If URL was /war, make tier 1
  if (tier === undefined) {
    tier = 1;
  }
  return (
    <div>
      <Board tier={tier} />
      <Navigation />
    </div>
  );
};

export default AllianceWar;
