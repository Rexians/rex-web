import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { getChamp } from "../../api/Roster";
import "../../styles/roster/ChampPage.css";

const ChampPage = () => {
  var { champid, tier } = useParams();
  const [champStats, setChampStats] = useState({});

  // Get champ stats based on selected champ
  // Assign it to a state
  const getChampStats = async () => {
    var response = await getChamp(champid, tier);
    response = response["champ_info"];
    var stats = {
      champName: response["champ_name"],
      champClass: response["champ_class"],
      tier: response["tier"],
      rank: response["rank"],
      prestige: response["prestige"],
      img: response["champ_img"],
    };
    setChampStats(stats);
  };

  useEffect(() => {
    getChampStats();
  }, {});

  return (
    <div className="champ-container">
      <img
        className="champ-img"
        id={champStats["champClass"]}
        src={champStats["img"]}
        alt="None"
      />
    </div>
  );
};

export default ChampPage;
