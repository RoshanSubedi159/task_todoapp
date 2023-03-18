import React from "react";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

const Header = () => {
  const navigate = useNavigate();
  const [isLogged, setIsLogged] = useState(localStorage.getItem("email"));

  return (
    <div className="app-header">
      <h1>Idea Vault</h1>
      {isLogged ? (
        <button
          onClick={() => {
            localStorage.clear();
            navigate("/login");
          }}
        >
          Logout
        </button>
      ) : (
        ""
      )}
    </div>
  );
};

export default Header;
