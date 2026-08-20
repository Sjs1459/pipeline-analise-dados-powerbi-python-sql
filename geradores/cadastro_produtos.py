import psycopg2
from faker import Faker
import os
from dotenv import load_dotenv
import random

load_dotenv()
conexao = psycopg2.connect(
     dbname = os.getenv("DB_NAME"),
     user = os.getenv("DB_USER"),
     password = os.getenv("DB_PASSWORD"),
     host = os.getenv("DB_HOST"),
     port = os.getenv("DB_PORT")
)

cursor = conexao.cursor()
cursor.execute("SELECT MAX(id_produto) FROM produtos")
ultimo_id = cursor.fetchone()[0]
qt_produtos = int(input("Quantos produtos deseja cadastrar no estoque?"))
base_id = 0 if ultimo_id is None else ultimo_id

p_hospitalar = [("Luva de Procedimento M (cx 100)", 1, 28.9)]
for i in (len(p_hospitalar)):
 estoque = random.randint(1,300)
 id_produto = base_id + 1
q_inserir_produtos = "INSERT id_produto, nome_produto, id_categoria, preco_estoque"

cursor.executemany()
