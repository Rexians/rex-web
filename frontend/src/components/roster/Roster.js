import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Nav, Navbar, Container } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlusSquare } from "@fortawesome/free-regular-svg-icons";
import { getChampsDisplay } from "../../api/Roster";
import AddChamp from "./AddChamp";
import Navigation from "../Navigation";
import "../../styles/roster/Roster.css";
import "../../styles/roster/ChampImgs.css";

const Roster = () => {
  // Add champ state
  const [isOpen, setIsOpen] = useState(false);

  // Prestige and Number of champs state
  const [prestige, setPrestige] = useState(0);
  const [champsCount, setChampsCount] = useState(0);

  const [champImgs, setChampImgs] = useState([]);

  // State to only load the roster once
  const [onLoad, setOnLoad] = useState(false);

  var navigate = useNavigate();

  // Called when image is clicked
  // Get selected champ and naviage to its champ page
  const selectChamp = (event) => {
    var champInfo = JSON.parse(event.target.getAttribute("champid"));
    navigate(`./${champInfo["champId"]}/${champInfo["tier"]}`);
  };

  // Get champ images and map them into image element
  const setRosterPage = async () => {
    setOnLoad(true);
    var response = await getChampsDisplay();

    if (response["display_info"] != null) {
      var lstChampImages = response["display_info"].map((champDisplay) => (
        <img
          onClick={selectChamp}
          className={`tier-${champDisplay["tier"]}`}
          id={champDisplay["champ_class"]}
          src={champDisplay["champ_img"]}
          alt="Not able to load..."
          key={`${champDisplay["champ_img"]}/${champDisplay["tier"]}`}
          champid={JSON.stringify({
            champId: champDisplay["champ_id"],
            tier: champDisplay["tier"],
          })}
        ></img>
      ));
      setChampsCount(lstChampImages.length);
      setChampImgs(lstChampImages);
    }
  };

  // Re render when image is added
  useEffect(() => {
    // On initial load, get all champs from roster
    // If champ is added, update champ counter by 1
    if (window.localStorage.getItem("logged") === "true") {
      if (!onLoad) {
        setRosterPage();
      } else {
        if (champsCount !== champImgs.length) setChampsCount(champsCount + 1);
      }
    }
  }, [champImgs]);

  return (
    <div>
      {window.localStorage.getItem("logged") === "true" ? (
        <div className="roster-container">
          <Container>
            <Nav.Item className="roster-prestige">{`Prestige: ${prestige}`}</Nav.Item>
            <Nav.Item className="roster-champ">{`Champions: ${champsCount}`}</Nav.Item>
            <FontAwesomeIcon
              title="Add"
              className="add-icon"
              onClick={() => setIsOpen(true)}
              icon={faPlusSquare}
            ></FontAwesomeIcon>
          </Container>
          <Navbar.Brand id="roster-title" className="roster-title">
            Roster
          </Navbar.Brand>
          <hr className="hr-left"></hr>
          <hr className="hr-right"></hr>
          {isOpen ? (
            <AddChamp
              setIsOpen={setIsOpen}
              champImgs={champImgs}
              setChampImgs={setChampImgs}
            />
          ) : null}
          {champImgs}
        </div>
      ) : (
        <div className="roster-login-message">
          You must be logged in to access roster
        </div>
      )}
      <Navigation />
    </div>
  );
};

export default Roster;
