import { useEffect, useState } from "react";
import "./LogInteractionScreen.css";

const API_URL = "http://127.0.0.1:8000";

export default function LogInteractionScreen() {
  const [text, setText] = useState("");
  const [interactions, setInteractions] = useState([]);

  const fetchInteractions = async () => {
    const res = await fetch(`${API_URL}/interactions`);
    const data = await res.json();
    setInteractions(data);
  };

  useEffect(() => {
    fetchInteractions();
  }, []);

  const submitInteraction = async (e) => {
    e.preventDefault();
    if (!text.trim()) return;

    await fetch(`${API_URL}/log-interaction`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    setText("");
    fetchInteractions();
  };

  const deleteAll = async () => {
    await fetch(`${API_URL}/interactions`, { method: "DELETE" });
    setInteractions([]);
  };

  return (
    <div className="container">
      <h2>Customer Relationship Management – Interactions</h2>

      <form onSubmit={submitInteraction}>
        <input
          className="interaction-input"
          placeholder="Enter customer interaction..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button className="interaction-button">Analyze</button>
      </form>

      <button className="delete-button" onClick={deleteAll}>
        Delete All
      </button>

      <table className="interactions-table">
        <thead>
          <tr>
            <th>Text</th>
            <th>AI Summary</th>
            <th>Sentiment</th>
          </tr>
        </thead>

        <tbody>
          {interactions.map((item) => (
            <tr key={item.id}>
              <td>{item.text}</td>
              <td>{item.summary || "Processing..."}</td>
              <td>
                <span
                  className={`badge ${
                    item.sentiment ? item.sentiment.toLowerCase() : "neutral"
                  }`}
                >
                  {item.sentiment || "Neutral"}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
