# backend/src/services/auth.py
from authlib.integrations.flask_client import OAuth
import jwt
import os
from datetime import datetime, timedelta

oauth = OAuth()
google_oauth = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'}
)

facebook_oauth = oauth.register(
    name='facebook',
    client_id=os.getenv('FACEBOOK_CLIENT_ID'),
    client_secret=os.getenv('FACEBOOK_CLIENT_SECRET'),
    authorize_url='https://www.facebook.com/v12.0/dialog/oauth',
    access_token_url='https://graph.facebook.com/v12.0/oauth/access_token',
    userinfo_endpoint='https://graph.facebook.com/v12.0/me',
    client_kwargs={'scope': 'email'}
)

def generate_jwt(user_id: str, role: str) -> str:
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=1),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')