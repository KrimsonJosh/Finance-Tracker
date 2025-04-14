import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Signup from './pages/Signup';

function App() {
  const isLoggedIn = !!document.cookie.includes('session');
  return (
    <Router>
      <div className = "bg-gray-100 min-h-screen">
        <Routes>
          {/* Navigate to dashboard if logged in, else enter login page*/}
          <Route path = "/" element={isLoggedIn ? <Navigate to ="/dashboard"/> : <Login />} />
          <Route path = "/signup" element = {<Signup />} />
          <Route path = "/dashboard" element = {isLoggedIn ? <Dashboard /> : <Navigate to = "/" />} /> 
        </Routes>
      </div>
    </Router>
  )
}

export default App
