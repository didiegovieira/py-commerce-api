import os
from src.infra.web.flask_adapter import app
from src.infra.database.user_repository_impl import UserRepositoryImpl
from src.core.usecases.create_user import CreateUser

def load_env():
    from dotenv import load_dotenv
    load_dotenv()
    print("Variáveis de ambiente carregadas.")

def configure_dependencies():
    user_repository = UserRepositoryImpl()
    create_user_usecase = CreateUser(user_repository=user_repository)
    app.config["create_user_usecase"] = create_user_usecase
    print("Dependências configuradas.")

def main():
    load_env()
    configure_dependencies()
    print("Iniciando o servidor...")
    app.run(host=os.getenv("HOST", "0.0.0.0"), port=int(os.getenv("PORT", 5000)), debug=True)

if __name__ == "__main__":
    main()
