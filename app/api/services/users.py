from app.api.schemas import UserCreate
from sqlalchemy.orm import Session
from app.api.repository import UserRepository


class UserService:
    user_repo = UserRepository()

    def create_user(self, user: UserCreate):
        return self.user_repo.create_user(user)
