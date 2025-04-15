import { Link } from 'react-router-dom';

interface Props {
    mode: 'login' | 'signup';
}

const AuthSwitch = ({ mode }: Props) => {
    return (
        <div className = "text-center mt-4 text-sm text-green-600">
            {mode === 'login' ? (
                <p>
                    Don't have an account?{' '}
                    <Link
                        to="/signup"
                        className="text-blue-500 hover:underline font-medium"
                    >
                        Signup
                    </Link>
                </p>
            ) : (
                <p>
                    Already have an account?{' '}
                    <Link
                        to="/login"
                        className="text-red-500 hover:underline font-medium"
                    >
                        Login
                    </Link>

                </p>
            )}
        </div>
    )
}

export default AuthSwitch;