import React, { useState } from "react";
import "./App.css";

function App() {
  const [code, setCode] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    try {
      const res = await fetch("http://localhost:8000/review", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ code }),
      });

      const data = await res.json();
      setResponse(data.result || data.detail || "No response");
    } catch (error) {
      setResponse("Error: " + error.message);
    }
  };

  return (
    <div className="App">
      <h1>🧠 Code Review with AI</h1>
      <textarea
        rows={10}
        cols={60}
        placeholder="Paste your Python code here..."
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />
      <br />
      <button onClick={handleSubmit}>Review</button>

      <h2>📝 Review Result:</h2>
      <pre>{response}</pre>
    </div>
  );
}

export default App;
