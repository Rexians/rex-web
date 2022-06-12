import { useState, useEffect } from "react";
import { Nav, Navbar, Container } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrashCan, faPlusSquare } from "@fortawesome/free-regular-svg-icons";
import { getChamps } from "../../api/Roster";
import AddChamp from "./AddChamp";
import Navigation from "../Navigation";
import "../../styles/Roster.css";

const Roster = () => {
  // Add champ state
  const [isOpen, setIsOpen] = useState(false);

  // Prestige and Number of champs state
  const [prestige, setPrestige] = useState(0);
  const [champsCount, setChampsCount] = useState(0);

  const [champImgs, setChampImgs] = useState([]);

  // State to only load the roster once
  const [onLoad, setOnLoad] = useState(false);

  // Get champ images and map them into image element
  const setRosterPage = async () => {
    setOnLoad(true);
    var response = await getChamps();
    if (response["champ_imgs"] != null) {
      var lstChampImages = response["champ_imgs"].map((champImg) => (
        <img src={champImg} alt={champImg} key={champImg}></img>
      ));
      setChampsCount(lstChampImages.length);
      setChampImgs(lstChampImages);
    }
  };

  // Re render when image is added
  useEffect(() => {
    // On initial load, get all champs from roster
    // If champ is added, update champ counter by 1
    if (!onLoad) {
      setRosterPage();
    } else {
      setChampsCount(champsCount + 1);
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
            <FontAwesomeIcon
              title="Delete"
              className="delete-icon"
              icon={faTrashCan}
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
