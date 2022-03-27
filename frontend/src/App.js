import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Test from "./components/Test";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/home" exact element={<Home />} />
        <Route path="/test" exact element={<Test />} />
      </Routes>
    </Router>
  );
}

export default App;
