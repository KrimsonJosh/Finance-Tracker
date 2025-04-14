import './App.css'
import Dashboard from './pages/Dashboard'
import React, { useState, useEffect } from "react"
function App() {

  return (
    <>
      <div className = "max-w-xl mx-auto p-4 bg-gray-100 min-h-screen">
        <h1 className="text-2xl font-bold mb-4">Intern Finance Tracker</h1>
        <Dashboard />
      </div>
    </>
  )
}

export default App
