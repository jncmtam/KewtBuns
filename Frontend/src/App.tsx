import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LoginButton from './components/LoginButton';
import Auth from './containers/Auth';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/auth/callback" element={<Auth />} />
        <Route path="/login" element={<div>Login Page</div>} />
        <Route path="/" element={<div className="flex flex-col justify-center items-center">Home Page</div>} />
      </Routes>
      <LoginButton />
    </BrowserRouter>
  );
};

export default App;
