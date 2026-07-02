#conexao com banco de dados

#instalar o drive conector
#MYSQL CONNECTOR
#o drive é um tradutor (PYTHON --> MYSQL)
import mysql.connector

def conectar():
    conexao=mysql.connector.connect(
    #o drive tenta abrir uma conexao
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'projetoindustrial',
    port = '3306'
    )
    return conexao