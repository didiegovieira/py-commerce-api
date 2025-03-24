# py-commerce-api

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**py-commerce-api** é uma API RESTful robusta e escalável projetada para um aplicativo de marketplace completo. Este projeto segue os princípios da **Clean Architecture**, garantindo modularidade, testabilidade e facilidade de manutenção.


## **Índice**
- [Recursos](#recursos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)


## **Recursos**
- Cadastro de usuários com validação de dados.
- Arquitetura modular baseada na **Clean Architecture**.
- Suporte para variáveis de ambiente com `.env`.
- Configuração pronta para Docker e Docker Compose.
- Testes unitários organizados por camadas.


## **Tecnologias Utilizadas**
- **Python 3.10**
- **Flask**: Framework web para construção da API.
- **Docker**: Para containerização do projeto.
- **Docker Compose**: Para orquestração de serviços.
- **pylint**: Para análise estática de código.
- **python-dotenv**: Para gerenciamento de variáveis de ambiente.


## **Estrutura do Projeto**
A estrutura do projeto segue os princípios da **Clean Architecture**:

```
py-commerce-api/
├── .env                  # Variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
├── docker-compose.yaml   # Configuração do Docker Compose
├── Dockerfile            # Configuração do Docker
├── Makefile              # Comandos úteis para automação
├── requirements.txt      # Dependências do projeto
├── cmd/                  # Pontos de entrada da aplicação
│   └── server/
│       └── main.py       # Inicialização do servidor Flask
├── src/                  # Código-fonte principal
│   ├── core/             # Regras de negócio (entidades e casos de uso)
│   ├── infra/            # Infraestrutura (banco de dados, web)
│   ├── interfaces/       # Interfaces (contratos para repositórios)
│   ├── services/         # Serviços externos (ex.: envio de e-mails)
│   └── tests/            # Testes organizados por camada
└── README.md             # Documentação do projeto
```


## **Instalação**

### **Pré-requisitos**
- Python 3.10 ou superior
- Docker e Docker Compose (opcional, para execução em contêineres)

### **Passos**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/py-commerce-api.git
   cd py-commerce-api
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # No Windows
   source venv/bin/activate      # No Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edite o arquivo `.env` conforme necessário.

5. Execute o servidor:
   ```bash
   python cmd/server/main.py
   ```

6. Acesse a API em: [http://localhost:5000](http://localhost:5000)


## **Uso**

### **Endpoints Disponíveis**
#### **POST /users**
Cadastra um novo usuário.

**Exemplo de Requisição:**
```bash
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}'
```

**Exemplo de Resposta:**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}
```


## **Testes**

### **Executando Testes**
1. Certifique-se de que o ambiente virtual está ativado.
2. Execute os testes com o `unittest`:
   ```bash
   python -m unittest discover -s src/tests
   ```


## **Comandos Úteis**

### **Makefile**
- Criar ambiente virtual:
  ```bash
  make venv
  ```
- Instalar dependências:
  ```bash
  make install
  ```
- Executar o servidor:
  ```bash
  make run
  ```
- Limpar o ambiente virtual:
  ```bash
  make clean
  ```

### **Docker**
- Construir a imagem Docker:
  ```bash
  docker build -t py-commerce-api .
  ```
- Executar com Docker Compose:
  ```bash
  docker-compose up
  ```


## **Contribuição**
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Adiciona minha feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.


## **Licença**
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
