// src/components/CommunityScreen.tsx

import "./community.css";
import { Link } from "react-router-dom";

const CommunityScreen = () => {
  return (
    <div className="community-container">
      <h1 className="community-title">
        <span role="img" aria-label="cow"></span> Researchers Community
      </h1>
      <p className="community-description">
        Welcome! Here you can share experiences, tips, and questions with other
        farmers.
      </p>
      <Link to="/home" className="back-link">
        ← Back to Cow List
      </Link>
    </div>
  );
};

export default CommunityScreen;
