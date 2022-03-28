import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import "./App.css";

function App() {
  return (
    <Router>
        <Routes>
          <Route path="/home" exact element={<Home />} />
        </Routes>
    </Router>
  );
}

export default App;
