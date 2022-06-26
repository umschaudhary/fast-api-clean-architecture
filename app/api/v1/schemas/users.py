from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """User Schema."""

    username: str
    email: EmailStr


class UserCreate(User):
    """User Create Schema."""

    password: str


class UserLogin(BaseModel):
    """User Login Schema."""

    email: EmailStr
    password: str


class ShowUser(User):
    """Show User Schema."""

    is_active: bool

    class Config:
        """Config Meta."""

        orm_mode = True


class UserLoginResponse(User):
    """User Login Response Schema."""

    access_token: str
    token_type: str

    class Config:
        """Config Meta."""

        orm_mode = True
