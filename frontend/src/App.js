import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";
import Home from "./components/Home";
import Login from "./components/Login";
import Authentication from "./components/Authentication";
import Roster from "./components/roster/Roster";
import ChampPage from "./components/roster/ChampPage";
import AllianceWar from "./components/alliancewar/AllianceWar";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

function App() {
  // Used to refresh app when user logs in
  const [logged, setLogged] = useState(false);

  return (
    <Router>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/auth"
          element={<Authentication setLogged={setLogged} />}
        />
        <Route exact path="/roster" element={<Roster />} />
        <Route exact path="/roster/:champid/:tier" element={<ChampPage />} />
        <Route exact path="/war" element={<AllianceWar />} />
        <Route exact path="/war/:tier" element={<AllianceWar />} />
      </Routes>
    </Router>
  );
}

export default App;
