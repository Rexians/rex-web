import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Login from "./components/Login";
import AllianceWar from "./components/alliancewar/AllianceWar";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/home" exact element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route exact path="/war" element={<AllianceWar />} />
        <Route path="/war/:tier" element={<AllianceWar />} />
      </Routes>
    </Router>
  );
}

export default App;
