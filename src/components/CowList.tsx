// components/CowList.tsx

import React from "react";
import { Link } from "react-router-dom";
import "./CowList.css";

const cows = [
  {
    name: "Brahman",
    origin: "India",
    description: "Known for heat tolerance and resistance to insects.",
    image: "/images/brahman.jpg",
  },
  {
    name: "Jersey",
    origin: "Jersey Island",
    description: "Popular for high butterfat content in milk.",
    image: "/images/jersey.jpg",
  },
  {
    name: "Gir",
    origin: "India",
    description: "One of the principal Zebu breeds, used for milk production.",
    image: "/images/gir.jpg",
  },
];

const CowList: React.FC = () => {
  return (
    <div className="cowlist-container">
      <h1 className="cowlist-title">🐄 Cow Breed Knowledge Hub</h1>

      <div className="cowlist-nav-buttons">
        <Link to="/community" className="cowlist-button">
          👥 Community
        </Link>
        <Link to="/research" className="cowlist-button">
          🔬 Research Hub
        </Link>
      </div>

      {cows.map((cow, index) => (
        <div className="cowlist-card" key={index}>
          <img src={cow.image} alt={cow.name} className="cowlist-image" />
          <h3>{cow.name}</h3>
          <p>
            <strong>Origin:</strong> {cow.origin}
          </p>
          <p>
            <strong>Description:</strong> {cow.description}
          </p>
        </div>
      ))}
    </div>
  );
};

export default CowList;
