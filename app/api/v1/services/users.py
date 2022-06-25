from sqlalchemy.orm import Session
from app.api.v1.schemas import UserCreate
from app.api.v1.repository import UserRepository


class UserService:
    user_repo = UserRepository()

    def create_user(self, user: UserCreate, db: Session):
        return self.user_repo.create_user(user, db)
