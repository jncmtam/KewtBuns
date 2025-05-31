import React from "react";
import { useAuthStore } from "../store/auth";
import { loginWithGoogle, loginWithFacebook } from "../services/auth";

const LoginButton: React.FC = () => {
  const { user } = useAuthStore();

  return (
    <div className="flex flex-col items-center justify-center p-6 space-y-4 bg-white rounded-2xl shadow-md w-full max-w-sm mx-auto">
      {user ? (
        <p className="text-lg font-semibold text-gray-800">
          Welcome, {user.email}
        </p>
      ) : (
        <>
          <button
            onClick={loginWithGoogle}
            className="w-full bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded-xl transition"
          >
            Sign in with Google
          </button>
          <button
            onClick={loginWithFacebook}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-xl transition"
          >
            Sign in with Facebook
          </button>
        </>
      )}
    </div>
  );
};

export default LoginButton;
