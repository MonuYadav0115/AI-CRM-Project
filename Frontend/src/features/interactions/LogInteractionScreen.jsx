// src/features/logInteraction/LogInteractionScreen.jsx
import { useState, useEffect } from "react";
import "./LogInteractionScreen.css";

export default function LogInteractionScreen() {
  const [text, setText] = useState("");
  const [interactions, setInteractions] = useState([]);

  const backendUrl = "http://127.0.0.1:8000";

  useEffect(() => {
    fetchInteractions();
  }, []);

  const fetchInteractions = async () => {
    try {
      const res = await fetch(`${backendUrl}/interactions`);
      const data = await res.json();
      setInteractions(data);
    } catch (err) {
      console.error("Failed to fetch interactions", err);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;

    try {
      await fetch(`${backendUrl}/log-interaction`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      setText("");
      fetchInteractions();
    } catch (err) {
      console.error("Failed to log interaction", err);
    }
  };

  const deleteAll = async () => {
    if (!window.confirm("Delete all interactions?")) return;

    try {
      await fetch(`${backendUrl}/interactions`, { method: "DELETE" });
      setInteractions([]);
    } catch (err) {
      console.error("Failed to delete interactions", err);
    }
  };

  return (
    <div className="container">
      <h2>Log Doctor Interaction</h2>

      <form onSubmit={handleSubmit}>
        <input
          className="interaction-input"
          placeholder="Enter doctor interaction"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button type="submit" className="interaction-button">
          Log Interaction
        </button>
      </form>

      <button className="delete-button" onClick={deleteAll}>
        Delete All Interactions
      </button>

      <h2>All Interactions</h2>

      <table className="interactions-table">
        <thead>
          <tr>
            <th>Text</th>
            <th>Summary</th>
            <th>Sentiment</th>
          </tr>
        </thead>
        <tbody>
          {interactions.length === 0 ? (
            <tr>
              <td colSpan="3" style={{ textAlign: "center" }}>
                No interactions yet
              </td>
            </tr>
          ) : (
            interactions.map((i) => (
              <tr key={i.id}>
                <td>{i.text}</td>
                <td>{i.summary}</td>
                <td>
                  <span className={`badge ${i.sentiment.toLowerCase()}`}>
                    {i.sentiment}
                  </span>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
