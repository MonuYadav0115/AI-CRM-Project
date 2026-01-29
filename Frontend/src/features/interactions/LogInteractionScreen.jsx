import { useState, useEffect } from "react";
import "./LogInteractionScreen.css";

export default function LogInteractionScreen() {
  const [text, setText] = useState("");
  const [interactions, setInteractions] = useState([]);
  const [message, setMessage] = useState("");

  const backendUrl = "http://127.0.0.1:8000";


  useEffect(() => {
    fetch(`${backendUrl}/api/message`)
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(console.error);

    fetchInteractions();
  }, []);

 
  const fetchInteractions = () => {
    fetch(`${backendUrl}/interactions`)
      .then((res) => res.json())
      .then((data) => setInteractions(data))
      .catch(console.error);
  };


  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;

    try {
      const res = await fetch(`${backendUrl}/log-interaction`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      if (res.ok) {
        setText("");
        fetchInteractions();
      }
    } catch (err) {
      console.log(err);
    }
  };

  const deleteAllInteractions = async () => {
    if (!window.confirm("Delete all interaction history?")) return;

    try {
      const res = await fetch(`${backendUrl}/interactions`, {
        method: "DELETE",
      });

      if (res.ok) {
        setInteractions([]);
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="container">
      <h2>{message}</h2>

      <form onSubmit={handleSubmit} className="interaction-form">
        <input
          type="text"
          placeholder="Enter interaction (e.g. Doctor was interested in medicine)"
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="interaction-input"
        />
        <button type="submit" className="interaction-button">
          Log Interaction
        </button>
      </form>

      <button className="delete-button" onClick={deleteAllInteractions}>
        Delete All History
      </button>

      <h3>All Interactions</h3>

      <table className="interactions-table">
        <thead>
          <tr>
            <th>Text</th>
            <th>Summary</th>
            <th>Sentiment</th>
          </tr>
        </thead>
        <tbody>
          {interactions.map((i) => (
            <tr key={i.id}>
              <td>{i.text}</td>
              <td>{i.summary || "-"}</td>
              <td>
                <span className={`badge ${i.sentiment?.toLowerCase()}`}>
                  {i.sentiment}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
