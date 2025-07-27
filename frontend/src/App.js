import React, { useState, useEffect } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import PortfolioHome from "./components/PortfolioHome";
import { Toaster } from "./components/ui/toaster";

function App() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulate loading time for smooth transition
    const timer = setTimeout(() => {
      setLoading(false);
    }, 1000); // Reduced from 2000 to 1000ms

    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="loader">
          <div className="loader-ring"></div>
          <div className="loader-text">Loading Portfolio...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<PortfolioHome />} />
        </Routes>
      </BrowserRouter>
      <Toaster />
    </div>
  );
}

export default App;