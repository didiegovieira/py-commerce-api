from flask import Flask, request, jsonify
from src.core.usecases.create_user import CreateUser
from src.infra.database.user_repository_impl import UserRepositoryImpl

app = Flask(__name__)
user_repository = UserRepositoryImpl()
create_user_usecase = CreateUser(user_repository=user_repository)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = create_user_usecase.execute(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email']
    )
    return jsonify({"id": user.id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email})

if __name__ == '__main__':
    app.run(debug=True)
