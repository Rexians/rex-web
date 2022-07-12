import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { getChamp } from "../../api/Roster";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faArrowAltCircleLeft,
  faStar,
} from "@fortawesome/free-regular-svg-icons";
import "../../styles/roster/ChampPage.css";

const ChampPage = () => {
  var wordNumbers = {
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
  };

  var { champid, tier } = useParams();
  const [champStats, setChampStats] = useState({});
  var navigate = useNavigate();

  // Get champ stats based on selected champ
  // Assign it to a state
  const getChampStats = async () => {
    var response = await getChamp(champid, tier);
    response = response["champ_info"];
    var stats = {
      champName: response["champ_name"],
      champClass: response["champ_class"],
      sig: response["sig"],
      level: response["level"],
      tier: response["tier"],
      rank: response["rank"],
      prestige: response["prestige"],
      img: response["champ_img"],
    };
    setChampStats(stats);
  };

  useEffect(() => {
    getChampStats();
  }, []);

  // When back clicked, go to roster page
  const goBack = () => {
    navigate("/roster");
  };

  const setStars = () => {
    var stars = [];
    for (var i = 1; i <= champStats["tier"]; i++) {
      stars.push(
        <FontAwesomeIcon
          icon={faStar}
          className="champ-stars"
          id={champStats["sig"] ? "awakened-stars" : "unawakened-stars"}
          key={i}
        />
      );
    }
    return stars;
  };

  return (
    <div className="champ-container">
      <div
        className="champ-name-border"
        id={`${wordNumbers[champStats["tier"]]}-border`}
      >
        <div className="champ-name-container">
          <h1
            className="champ-name"
            id={`${wordNumbers[champStats["tier"]]}-name`}
          >
            {champStats["champName"]}
          </h1>
        </div>
      </div>
      <div className="back-button-border">
        <div className="back-button">
          <FontAwesomeIcon
            icon={faArrowAltCircleLeft}
            className="back-button-icon"
            onClick={goBack}
          />
        </div>
      </div>
      <div className="wrapper">
        <div className="stats-bar">
          <div className="stats-inner-page">
            <div className="champ-stats">{setStars()}</div>
            <div className="champ-stats">
              <div>BASE PRESTIGE</div>
              <div className="champ-stats-value">{champStats["prestige"]}</div>
            </div>
            <div className="champ-stats">
              <div>SIGNATURE LEVEL</div>
              <div className="champ-stats-value">{champStats["sig"]}</div>
            </div>
            <div className="champ-stats">
              <div>TIER</div>
              <div className="champ-stats-value">{champStats["tier"]}</div>
            </div>
            <div className="champ-stats">
              <div>RANK</div>
              <div className="champ-stats-value">{champStats["rank"]}</div>
            </div>
            <div className="champ-stats">
              <div>LEVEL</div>
              <div className="champ-stats-value">{champStats["level"]}</div>
            </div>
          </div>
        </div>
        <img
          className="champ-img"
          id={champStats["champClass"]}
          src={champStats["img"]}
          alt="None"
        />
      </div>
    </div>
  );
};

export default ChampPage;
