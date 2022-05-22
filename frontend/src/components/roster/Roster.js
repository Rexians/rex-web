import { useState } from "react";
import { Nav, Navbar, Container } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrashCan, faPlusSquare } from "@fortawesome/free-regular-svg-icons";
import Navigation from "../Navigation";
import abomination from "../../assets/champs/abomination.png";
import "../../styles/roster/Roster.css";

const Roster = () => {
  const [prestige, setPrestige] = useState(0);
  const [champs, setChamps] = useState(0);
  return (
    <div>
      <div className="roster-container">
        <Container>
          <Nav.Item className="roster-prestige">{`Prestige: ${prestige}`}</Nav.Item>
          <Nav.Item className="roster-champ">{`Champions: ${champs}`}</Nav.Item>
          <FontAwesomeIcon
            title="Add"
            className="add-icon"
            icon={faPlusSquare}
          ></FontAwesomeIcon>
          <FontAwesomeIcon
            title="Delete"
            className="delete-icon"
            icon={faTrashCan}
          ></FontAwesomeIcon>
        </Container>
        <Navbar.Brand className="roster-title">Roster</Navbar.Brand>
        <Container>
          <hr className="hr-left"></hr>
          <hr className="hr-right"></hr>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
          <img src={abomination} alt="Abom"></img>
        </Container>
      </div>
      <Navigation />
    </div>
  );
};

export default Roster;
