# backend/src/api/auth.py
from flask import Blueprint, redirect, request, jsonify
from dotenv import load_dotenv
load_dotenv()
from ..services.auth_service import google_oauth, facebook_oauth, generate_jwt
from ..repositories.user_repo import UserRepository
from ..models.user import User
import os

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/google/login', methods=['GET'])
def google_login():
    redirect_uri = os.getenv('GOOGLE_REDIRECT_URI')
    return google_oauth.authorize_redirect(redirect_uri)

@auth_bp.route('/google/callback', methods=['GET'])
def google_callback():
    try:
        token = google_oauth.authorize_access_token()
        user_info = google_oauth.parse_id_token(token)
        email = user_info['email']
        oauth_id = f"google_{user_info['sub']}"

        user_repo = UserRepository()
        user = user_repo.get_by_oauth_id(oauth_id)
        if not user:
            user = user_repo.create(email=email, oauth_id=oauth_id, role='customer')

        jwt_token = generate_jwt(user.id, user.role)
        return jsonify({'token': jwt_token, 'user': {'id': user.id, 'email': user.email, 'role': user.role}})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/facebook/login', methods=['GET'])
def facebook_login():
    redirect_uri = os.getenv('FACEBOOK_REDIRECT_URI')
    return facebook_oauth.authorize_redirect(redirect_uri)

@auth_bp.route('/facebook/callback', methods=['GET'])
def facebook_callback():
    try:
        token = facebook_oauth.authorize_access_token()
        user_info = facebook_oauth.get('me?fields=id,email').json()
        email = user_info.get('email')
        oauth_id = f"facebook_{user_info['id']}"

        if not email:
            return jsonify({'error': 'Email not provided by Facebook'}), 400

        user_repo = UserRepository()
        user = user_repo.get_by_oauth_id(oauth_id)
        if not user:
            user = user_repo.create(email=email, oauth_id=oauth_id, role='customer')

        jwt_token = generate_jwt(user.id, user.role)
        return jsonify({'token': jwt_token, 'user': {'id': user.id, 'email': user.email, 'role': user.role}})
    except Exception as e:
        return jsonify({'error': str(e)}), 400