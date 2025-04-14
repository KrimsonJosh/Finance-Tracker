import './App.css'
import Dashboard from './components/Dashboard'
import FinancePieChart from './components/FinancePIeChart'
import React, { useState, useEffect } from "react"
function App() {

  const mockData = [
    { category: 'food', amount: 150},
    { category: 'rent', amount: 500},
    { category: 'utils', amount: 100},
    { category: 'entertainemtn etc', amount: 200},
    { category: 'tuitin/savings', amount: 200},
  ];

  return (
    <>
      <div className = "max-w-xl mx-auto p-4 bg-gray-100 min-h-screen">
        <h1 className="text-2xl font-bold mb-4">Intern Finance Tracker</h1>
        <Dashboard />
        <FinancePieChart data = {mockData} />
      </div>
    </>
  )
}

export default App
