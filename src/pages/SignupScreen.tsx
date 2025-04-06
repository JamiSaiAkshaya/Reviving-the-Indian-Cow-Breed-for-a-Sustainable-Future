import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { supabase } from "../lib/supabaseClient"; // Supabase client

const SignupScreen: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSignup = async () => {
    const { error } = await supabase.auth.signUp({ email, password });
    if (error) {
      setError(error.message);
    } else {
      navigate("/login"); // Redirect to login after successful signup
    }
  };

  return (
    <div className="signup-screen">
      <h1>Signup</h1>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleSignup}>Sign Up</button>
      {error && <p className="error">{error}</p>}
    </div>
  );
};

export default SignupScreen;
