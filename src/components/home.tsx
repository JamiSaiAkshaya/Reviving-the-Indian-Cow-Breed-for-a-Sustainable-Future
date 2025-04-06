// components/Home.tsx
import React from "react";
import { Link } from "react-router-dom";

const Home: React.FC = () => {
  return (
    <div style={{ padding: "1rem", textAlign: "center" }}>
      <h1>🐄 Welcome to the Cow Breed App</h1>
      <p>Your hub for learning and sharing knowledge about cow breeds.</p>
      <Link to="/cows">Explore Cow Breeds</Link>
    </div>
  );
};

export default Home;
