import axios from 'axios';

const API_URL = 'http://localhost:6969/api/auth';

export const loginWithGoogle = () => {
  window.location.href = `${API_URL}/google/login`;
};

export const loginWithFacebook = () => {
  window.location.href = `${API_URL}/facebook/login`;
};

export const handleCallback = async (callbackUrl: string) => {
  try {
    const response = await axios.get(callbackUrl, { withCredentials: true });
    return response.data; // { token, user }
  } catch (error) {
    throw new Error('Authentication failed');
  }
};
