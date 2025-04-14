import { useState } from 'react';
import api from '../api';

const Signup = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSignup = async () => {
        try {
            const res = await api.post('/signup', {
                username,
                password,
            });
            alert (res.data.message);
        } catch(err: any){
            alert(err.response?.data?.error || "Signup failed");
        }
    };

    return (
        <div className = "p-4">
            <h2 className = "text-xl font-bold mb-4">Signup</h2>
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
                onClick = {handleSignup}
                className = "bg-blue-500 text-white px-4 py-2 rounded"
            ></button>
        </div>
    );
};

export default Signup