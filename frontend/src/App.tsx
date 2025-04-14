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
          <Route path = "/" element = {<Navigate to= "/signup" />} />
          <Route path = "/login" element = {<Login/>} />
          <Route path = "/signup" element = {<Signup />} />
          <Route 
            path = "/dashboard" 
            element = {isLoggedIn ? <Dashboard /> : <Navigate to = "/login" />} /> 
        </Routes>
      </div>
    </Router>
  )
}

export default App
