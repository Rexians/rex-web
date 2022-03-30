import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";

import Home from "./components/Home";
import AllianceWar from "./components/alliancewar/AllianceWar";

import "./App.css";

function App() {
  const [sidebarState, setSidebarState] = useState(false);

  return (
    <Router>
        <Routes>
          <Route path="/home" exact element={<Home sidebarState={sidebarState} setSidebarState={setSidebarState}/>}/>
          <Route path="/war" exact element={<AllianceWar sidebarState={sidebarState} setSidebarState={setSidebarState}/>}/>
        </Routes>
    </Router>
  );
}

export default App;
