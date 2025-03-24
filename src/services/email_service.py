class EmailService:
    def __init__(self):
        pass

    def send_email(self, to: str, subject: str, body: str):
        print(f"Enviando e-mail para {to} com assunto '{subject}' e corpo '{body}'")
