import psycopg2
import os
from dotenv import load_dotenv
from random import choice
from datetime import date

load_dotenv()

conexao = psycopg2.connect(
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT")
)


def criar_pedidos():
 cursor = conexao.cursor()

 query_criar_pedido = 'SELECT max(id_pedido) from pedidos'
 cursor.execute(query_criar_pedido)
 ultimo_pedido = cursor.fetchone()[0]
 if ultimo_pedido == None:
   ultimo_pedido = 1
 else: 
   novo_pedido = ultimo_pedido + 1

 q_selecionar_cliente = 'SELECT id_cliente FROM clientes'
 cursor.execute(q_selecionar_cliente)
 ids_clientes = cursor.fetchall()
 id_cliente = choice(ids_clientes)[0]

 q_selecionar_idvendedor = 'SELECT id_vendedor from vendedores'
 cursor.execute(q_selecionar_idvendedor)
 id_vendedores = cursor.fetchall()
 id_vendedor = choice(id_vendedores)

 data_pedido = date.today()
 status = choice(['entregue', 'cancelado', 'enviado', 'processando'])


 q_inserir_vendedor = 'insert into pedidos (id_pedido, id_cliente, id_vendedor, data_pedido, status) values (%s,%s,%s,%s,%s);'
 cursor.execute(q_inserir_vendedor, (novo_pedido, id_cliente, id_vendedor,data_pedido, status))

 conexao.commit()
 cursor.close()
 conexao.close()