import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Login from "./components/Login";
import Authentication from "./components/Authentication";
import AllianceWar from "./components/alliancewar/AllianceWar";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/auth" element={<Authentication />} />
        <Route exact path="/war" element={<AllianceWar />} />
        <Route path="/war/:tier" element={<AllianceWar />} />
      </Routes>
    </Router>
  );
}

export default App;
