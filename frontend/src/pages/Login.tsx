import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import api from '../api';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async () => {
        try {
            const res = await api.post('/login', {
                username, 
                password,
            });
            localStorage.setItem('isLoggedIn', 'true');
            navigate('/dashboard');
            alert(res.data.message);
        } catch (err: any) {
            alert(err.response?.data?.error || 'Login failed');
        }
    };

    return (
        <div className = "p-4">
            <h2 className = "text-xl font-bold mb-4">Login</h2>
            <input
                className = "border p-2 mb-2 w-full"
                placeholder = "Username"
                value = {username}
                onChange = {(e) => setUsername(e.target.value)}
            />
            <input
                className="border p-2 mb-4 w-full"
                placeholder="Password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button
                onClick = {handleLogin}
                className = "bg-blue-500 text-white px-4 py-2 rounded"
            >
                Login
            </button>
        </div>
    );
};

export default Login;