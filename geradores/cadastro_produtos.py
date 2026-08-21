import psycopg2
import os
from dotenv import load_dotenv 
import random
from dados_produtos import p_hospitalar 

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
base_id = 0 if ultimo_id is None else ultimo_id

qt_produtos = len(p_hospitalar)
for i in range(qt_produtos):
 id_produto = base_id + 1 + i
 nome_produto = p_hospitalar[i][0]
 id_categoria = p_hospitalar[i][1]
 preco = p_hospitalar[i][2]
 estoque = random.randint(1,300)


q_inserir_produtos = "INSERT into produtos(id_produto, nome_produto, id_categoria, preco, estoque) VALUES (%s,%s,%s,%s,%s)" 
cursor.execute(q_inserir_produtos, id_produto, nome_produto, id_categoria, preco, estoque )

conexao.commit()
cursor.close()
conexao.close()
