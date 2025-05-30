# backend/src/repositories/user_repo.py
from ..models.user import User, db
import uuid

class UserRepository:
    def get_by_oauth_id(self, oauth_id: str) -> User:
        return User.query.filter_by(oauth_id=oauth_id).first()

    def create(self, email: str, oauth_id: str, role: str = 'customer') -> User:
        user = User(id=str(uuid.uuid4()), email=email, oauth_id=oauth_id, role=role)
        db.session.add(user)
        db.session.commit()
        return user