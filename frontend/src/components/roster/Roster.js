import { useState } from "react";
import { Nav, Navbar, Container } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrashCan, faPlusSquare } from "@fortawesome/free-regular-svg-icons";
import AddChamp from "./AddChamp";
import Navigation from "../Navigation";
import abomination from "../../assets/champs/abomination.png";
import "../../styles/Roster.css";

const Roster = () => {
  // Add champ state
  const [isOpen, setIsOpen] = useState(false);

  const [prestige, setPrestige] = useState(20000);
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
        {isOpen ? <AddChamp setIsOpen={setIsOpen} /> : null}
        <img src={abomination} alt="Abom"></img>
      </div>
      <Navigation />
    </div>
  );
};

export default Roster;
