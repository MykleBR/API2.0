import mysql.connector

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'testaxyadb'
}

# Função para conectar ao banco de dados
def connect_db():
    return mysql.connector.connect(**db_config)
