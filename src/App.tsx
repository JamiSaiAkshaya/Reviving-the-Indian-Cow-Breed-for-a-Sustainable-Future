// src/App.tsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CowList from "./components/CowList";
import Community from "./components/Community";
import AddCow from "./components/AddCow";
import Home from "./components/home";
import Research from "./components/research"; // Importing Research page

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/cows" element={<CowList />} />
        <Route path="/community" element={<Community />} />
        <Route path="/add-cow" element={<AddCow />} />
        <Route path="/research" element={<Research />} /> {/* NEW ROUTE */}
      </Routes>
    </Router>
  );
};

export default App;
