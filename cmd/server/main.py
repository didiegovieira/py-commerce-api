import server

server.run()
# Path: cmd/server/server.py
def run():
    print('Server is running...')
# Path: cmd/client/main.py
import client

client.run()
# Path: cmd/client/client.py
def run():
    print('Client is running...')