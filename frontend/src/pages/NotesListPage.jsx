import React, { useState, useEffect } from "react";
import List_item from "../components/List_item";
import AddButton from "../components/AddButton";
import { TbNotes } from "react-icons/tb";
import { useNavigate } from "react-router-dom";

const NotesListPage = () => {
  let [notes, setNotes] = useState([]);
  const [isLogged, setIsLogged] = useState(localStorage.getItem("email"));
  const navigate = useNavigate();
  useEffect(() => {
    getNotes();
    if (!isLogged) {
      navigate("/login");
    }
  }, []);

  let getNotes = async () => {
    let response = await fetch("/api/notes/");
    let data = await response.json();
    setNotes(data);
  };

  return (
    <div className="notes">
      <div className="notes-header">
        <h2 className="notes-title" textalign="center">
          <TbNotes />
          Items
        </h2>
        <p className="notes-count">{notes.length}</p>
      </div>
      <div className="notes-list">
        {notes.map((note, index) => (
          <List_item key={index} note={note} />
        ))}
      </div>
      <AddButton />
    </div>
  );
};

export default NotesListPage;
