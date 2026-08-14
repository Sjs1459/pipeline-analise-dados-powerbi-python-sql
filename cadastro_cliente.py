import psycopg2
import os
from datetime import date
import random
from ibge.localidades import Estados, Municipios
from faker import Faker
from dotenv import load_dotenv

fake = Faker('pt-BR')

estados = Estados().json()
municipios = Municipios().json()
load_dotenv()
conexao = psycopg2.connect(
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT")
)


cursor = conexao.cursor()
q_ultimo_id_cliente = 'SELECT max(id_cliente) FROM clientes'
cursor.execute(q_ultimo_id_cliente)
ultimo_id_cliente = cursor.fetchone()[0]

if ultimo_id_cliente == None:
    ultimo_id_cliente = 1
else:
    id_cliente = ultimo_id_cliente + 1
    
nome = fake.company()
cidade = random.choice(municipios)
nome_cidade = cidade['nome']
estado = cidade['microrregiao']["mesorregiao"]['UF']['sigla']
email = fake.company_email()
data = date.today()
ativo = random.choice([True, False])

query_inserir_cliente = "insert into clientes (id_cliente, nome, cidade,estado, email, data_cadastro,ativo) " \
"values (%s, %s, %s, %s, %s, %s, %s)"

cursor.execute(query_inserir_cliente, (id_cliente, nome, nome_cidade,estado, email, data, ativo))

conexao.commit()

cursor.close()

conexao.close()
