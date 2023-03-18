import React from "react";
import { Link } from "react-router-dom";
// import { ReactComponent as Plus } from "../assets/plus.svg";
import { AiOutlineFileAdd } from "react-icons/ai";

const AddButton = () => {
  return (
    <Link to="/note/new" className="floating-button">
      <AiOutlineFileAdd size={30} />
    </Link>
  );
};

export default AddButton;
