from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:

    @static_method
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @static_method
    def get_hashed_password(plain_password):
        return pwd_context.hash(plain_password)
