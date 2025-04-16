import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';
import AuthSwitch from '../components/AuthSwitch';

const Login = ({ onLoginSuccess }: { onLoginSuccess: () => void }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        try {
            await api.post('/login', {
                username, 
                password,
            });
            onLoginSuccess();
            navigate('/dashboard');
        } catch (err: any) {
            setError(err.response?.data?.error || 'Login failed');
        }
    };

    return (
        <div className="p-4 max-w-md mx-auto">
            <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>
            {error && (
                <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                    {error}
                </div>
            )}
            <form onSubmit={handleLogin}>
                <input
                    className="border p-2 mb-2 w-full rounded"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <input
                    className="border p-2 mb-4 w-full rounded"
                    placeholder="Password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button
                    type="submit"
                    className="bg-blue-500 text-white px-4 py-2 rounded w-full hover:bg-blue-600"
                >
                    Login
                </button>
            </form>
            <AuthSwitch mode="login" />
        </div>
    );
};

export default Login;