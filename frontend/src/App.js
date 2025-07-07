import React, { useState } from "react";
import "./App.css";

function App() {
  const [code, setCode] = useState('');
  const [result, setResult] = useState('');

  const handleReview = async () => {
    try {
      const response = await fetch('http://localhost:8000/review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      });

      const data = await response.json();
      setResult(data.result || data.detail || 'No response.');
    } catch (error) {
      setResult('Error: Failed to fetch');
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center px-4">
      <h1 className="text-pink-400 text-xl font-semibold mb-4">💬 Code Review with AI</h1>

      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your Python code here..."
        className="w-full max-w-2xl h-52 p-4 text-sm bg-gray-800 text-white rounded-md border border-gray-600 focus:outline-none focus:ring-2 focus:ring-pink-500 resize-none mb-4"
      ></textarea>

      <button
        onClick={handleReview}
        className="mb-6 px-6 py-2 bg-indigo-600 text-white font-medium rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-400 transition"
      >
        Review
      </button>

      <div className="w-full max-w-2xl bg-gray-800 p-4 rounded-md border border-gray-700">
        <h2 className="text-pink-400 font-semibold mb-2">Review Result:</h2>
        <pre className="text-sm whitespace-pre-wrap">{result}</pre>
      </div>
    </div>
  );
}

export default App;
