import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = { sender: "user", text: message };
    setChat((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await axios.get(
        `${process.env.REACT_APP_API_URL}/ask`,
        {
          params: { question: message }
        }
      );

      const botMessage = {
        sender: "bot",
        text: response.data.response || "No response received."
      };

      setChat((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error("Error:", error);
      setChat((prev) => [
        ...prev,
        { sender: "bot", text: "Backend connection failed." }
      ]);
    }

    setMessage("");
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>☁️ AI Study Assistant</h1>

      <div className="chat-box">
        {chat.map((msg, index) => (
          <div
            key={index}
            className={msg.sender === "user" ? "user" : "bot"}
          >
            <strong>{msg.sender === "user" ? "You: " : "AI: "}</strong>
            {msg.text}
          </div>
        ))}

        {loading && <div className="bot">AI is thinking...</div>}
      </div>

      <div className="input-area">
        <input
          type="text"
          placeholder="Ask something..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
