import React from 'react';
import { useAuthStore } from '../store/auth';
import { loginWithGoogle, loginWithFacebook } from '../services/auth';

const LoginButton: React.FC = () => {
  const { user } = useAuthStore();

  return (
    <div>
      {user ? (
        <p>Welcome, {user.email}</p>
      ) : (
        <>
          <button onClick={loginWithGoogle}>Sign in with Google</button>
          <button onClick={loginWithFacebook}>Sign in with Facebook</button>
        </>
      )}
    </div>
  );
};

export default LoginButton;
