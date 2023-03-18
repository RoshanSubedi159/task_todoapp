import { HashRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Header from "./components/header.jsx";
import NotesListPage from "./pages/NotesListPage.jsx";
import NotePage from "./pages/NotePage.jsx";
import Login from "./components/LoginCom.jsx";
function App() {
  return (
    <Router>
      <div className="container dark">
        <div className="app">
          <Header />
          <Routes>
            <Route path="/" exact element={<NotesListPage />} />
            <Route path="/note/:id" element={<NotePage />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
