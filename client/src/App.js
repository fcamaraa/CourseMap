import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "./Home";
import ColumbiaPage from "./ColumbiaPage"; // Component for Columbia
import QueensPage from "./QueensPage"; // Component for Queens College

const App = () => {
  return (
    <Router>
      <div className="App">
        <nav>
          <Link to="/">Home</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/columbia" element={<ColumbiaPage />} />
          <Route path="/queens" element={<QueensPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
