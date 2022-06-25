from sqlalchemy.orm import Session
from app.api.v1.schemas import UserCreate
from app.models import User
from app.api.v1.repository import UserRepository


class UserService:
    user_repo = UserRepository()

    def create_user(self, user: UserCreate, db: Session) -> User:
        return self.user_repo.create_user(user, db)

    def get_user_by_email(self, email: str, db: Session) -> User:
        return self.user_repo.get_user_by_email(email, db)

    def authenticate_user(self, email: str, password: str, db: Session) -> User:
        return self.user_repo.authenticate_user(email, password, db)
