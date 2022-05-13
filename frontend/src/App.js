import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";
import Home from "./components/Home";
import Login from "./components/Login";
import Authentication from "./components/Authentication";
import AllianceWar from "./components/alliancewar/AllianceWar";
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
        <Route exact path="/war" element={<AllianceWar />} />
        <Route path="/war/:tier" element={<AllianceWar />} />
      </Routes>
    </Router>
  );
}

export default App;
