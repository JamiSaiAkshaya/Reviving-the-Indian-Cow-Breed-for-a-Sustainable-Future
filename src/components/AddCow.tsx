import React, { useEffect, useState } from "react";
import { supabase } from "../lib/supabaseClient";
import "./AddCow.css";

interface Cow {
  id: number;
  breed: string;
  origin: string;
  milk_yield: number;
  description: string;
}

const CowList: React.FC = () => {
  const [cows, setCows] = useState<Cow[]>([]);

  useEffect(() => {
    const fetchCows = async () => {
      const { data, error } = await supabase.from("cows").select("*");
      if (error) {
        console.error("Error fetching cows:", error.message);
      } else {
        setCows(data || []);
      }
    };

    fetchCows();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2
        style={{ fontSize: "24px", fontWeight: "bold", marginBottom: "20px" }}
      >
        All Cow Breeds
      </h2>

      {cows.length === 0 ? (
        <p style={{ color: "#555" }}>No cows found.</p>
      ) : (
        <ul style={{ listStyleType: "none", padding: 0 }}>
          {cows.map((cow) => (
            <li
              key={cow.id}
              style={{
                border: "1px solid #ccc",
                borderRadius: "8px",
                padding: "15px",
                marginBottom: "15px",
                backgroundColor: "#f9f9f9",
              }}
            >
              <p>
                <strong>Breed:</strong> {cow.breed}
              </p>
              <p>
                <strong>Origin:</strong> {cow.origin}
              </p>
              <p>
                <strong>Milk Yield:</strong> {cow.milk_yield} L/day
              </p>
              <p>
                <strong>Description:</strong> {cow.description}
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CowList;
