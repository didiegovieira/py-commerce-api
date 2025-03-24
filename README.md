# py-commerce-api

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**py-commerce-api** is a robust and scalable RESTful API designed for a complete marketplace application. This project follows the principles of **Clean Architecture**, ensuring modularity, testability, and maintainability.

## **Table of Contents**
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Contribution](#contribution)
- [License](#license)

## **Features**
- User registration with data validation.
- Modular architecture based on **Clean Architecture**.
- Support for environment variables using `.env`.
- Ready-to-use configuration for Docker and Docker Compose.
- Unit tests organized by layers.

## **Technologies Used**
- **Python 3.10**
- **Flask**: Web framework for building the API.
- **Docker**: For containerizing the project.
- **Docker Compose**: For orchestrating services.
- **pylint**: For static code analysis.
- **python-dotenv**: For managing environment variables.

## **Project Structure**
The project structure follows the principles of **Clean Architecture**:

```
py-commerce-api/
├── .env                  # Environment variables
├── .gitignore            # Files ignored by Git
├── docker-compose.yaml   # Docker Compose configuration
├── Dockerfile            # Docker configuration
├── Makefile              # Useful automation commands
├── requirements.txt      # Project dependencies
├── cmd/                  # Application entry points
│   └── server/
│       └── main.py       # Flask server initialization
├── src/                  # Main source code
│   ├── core/             # Business rules (entities and use cases)
│   ├── infra/            # Infrastructure (database, web)
│   ├── interfaces/       # Interfaces (repository contracts)
│   ├── services/         # External services (e.g., email sending)
│   └── tests/            # Tests organized by layer
└── README.md             # Project documentation
```

## **Installation**

### **Prerequisites**
- Python 3.10 or higher
- Docker and Docker Compose (optional, for running in containers)

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/py-commerce-api.git
   cd py-commerce-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   source venv/bin/activate      # On Linux/Mac
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment variables:
   - Copy the `.env.example` file to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit the `.env` file as needed.

5. Run the server:
   ```bash
   python cmd/server/main.py
   ```

6. Access the API at: [http://localhost:5000](http://localhost:5000)

## **Usage**

### **Available Endpoints**
#### **POST /users**
Registers a new user.

**Request Example:**
```bash
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}'
```

**Response Example:**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}
```

## **Tests**

### **Running Tests**
1. Ensure the virtual environment is activated.
2. Run the tests using `unittest`:
   ```bash
   python -m unittest discover -s src/tests
   ```

## **Useful Commands**

### **Makefile**
- Create a virtual environment:
  ```bash
  make venv
  ```
- Install dependencies:
  ```bash
  make install
  ```
- Run the server:
  ```bash
  make run
  ```
- Clean the virtual environment:
  ```bash
  make clean
  ```

### **Docker**
- Build the Docker image:
  ```bash
  docker build -t py-commerce-api .
  ```
- Run with Docker Compose:
  ```bash
  docker-compose up
  ```

## **Contribution**
Contributions are welcome! Follow the steps below to contribute:
1. Fork the repository.
2. Create a branch for your feature or fix:
   ```bash
   git checkout -b my-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add my feature"
   ```
4. Push to the remote repository:
   ```bash
   git push origin my-feature
   ```
5. Open a Pull Request.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.