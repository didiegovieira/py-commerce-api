.PHONY: venv install run clean

# Cria o ambiente virtual
venv:
	python -m venv venv

# Instala as dependências no ambiente virtual
install: venv
	venv/Scripts/pip install -r requirements.txt

# Executa o servidor
run:
	venv/Scripts/python cmd/server/main.py

# Limpa o ambiente virtual
clean:
	rm -rf venv

# Ativa o ambiente virtual
activate:
	source venv/Scripts/activate