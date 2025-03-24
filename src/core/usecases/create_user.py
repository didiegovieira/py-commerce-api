from src.interfaces.user_repository import UserRepository
from src.core.entities.user import User

class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, first_name: str, last_name: str, email: str) -> User:
        user = User(id=None, first_name=first_name, last_name=last_name, email=email)
        return self.user_repository.save(user)
