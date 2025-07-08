import React, { useState } from "react";
import "./App.css";

function App() {
  const [loading, setLoading] = useState(false);
  const [code, setCode] = useState('');
  const [result, setResult] = useState('');

  const handleReview = async () => {
    setLoading(true);
    setResult('');  

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
    } finally {
      setLoading(false);
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
        disabled={loading}
        className={`mb-2 px-6 py-2 font-medium rounded-md focus:outline-none transition ${
          loading
            ? 'bg-gray-500 cursor-not-allowed'
            : 'bg-indigo-600 hover:bg-indigo-700 text-white focus:ring-2 focus:ring-indigo-400'
        }`}
      >
        {loading ? 'Reviewing...' : 'Review'}
      </button>

      {loading && (
        <div className="flex items-center justify-center mb-4">
          <svg className="animate-spin h-6 w-6 text-pink-400" viewBox="0 0 24 24">
            <circle
              className="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              strokeWidth="4"
              fill="none"
            />
            <path
              className="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8v8z"
            />
          </svg>
          <span className="ml-2 text-pink-300">Analyzing code...</span>
        </div>
      )}



      <div className="w-full max-w-2xl bg-gray-800 p-4 rounded-md border border-gray-700">
        <h2 className="text-pink-400 font-semibold mb-2">Review Result:</h2>
        <pre className="text-sm whitespace-pre-wrap">{result}</pre>
      </div>
    </div>
  );
}

export default App;
