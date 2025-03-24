from src.interfaces.user_repository import UserRepository
from src.core.entities.user import User

class UserRepositoryImpl(UserRepository):
    def __init__(self):
        self.users = []  # Simulação de banco de dados em memória

    def save(self, user: User) -> User:
        user.id = len(self.users) + 1
        self.users.append(user)
        return user

    def find_by_email(self, email: str) -> User:
        for user in self.users:
            if user.email == email:
                return user
        return None
