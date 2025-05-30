import React, { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { handleCallback } from '../services/auth';
import { useAuthStore } from '../store/auth';

const Auth: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { setAuth } = useAuthStore();

  useEffect(() => {
    const handleAuthCallback = async () => {
      if (location.pathname === '/auth/callback') {
        try {
          const callbackUrl = `http://localhost:6969${location.pathname}${location.search}`;
          const { token, user } = await handleCallback(callbackUrl);
          setAuth(token, user);
          navigate('/'); // Redirect to homepage
        } catch (error) {
          console.error('Auth error:', error);
          navigate('/login'); // Redirect to login page on error
        }
      }
    };
    handleAuthCallback();
  }, [location, navigate, setAuth]);

  return <div>Loading...</div>;
};

export default Auth;
