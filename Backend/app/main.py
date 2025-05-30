# backend/src/main.py
from flask import Flask
from flask_cors import CORS
from .api.auth import auth_bp
from .models.user import db
from .services.auth_service import oauth
import os
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://minhtam:@localhost:5432/kewtielops'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
    
    db.init_app(app)
    oauth.init_app(app)
    CORS(app, origins=['http://localhost:3000']) # For Frontend access

    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=6969)
