import psycopg2
import os
from random import randint, choice
from dotenv import load_dotenv

load_dotenv()


conexao = psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"))


def cadastrar_itens_pedido():
 cursor = conexao.cursor()
 total_voltas = randint(1,3)

 for i in range(total_voltas):
  q_ultimo_id_item = 'SELECT max(id_item) FROM itens_pedido'
  cursor.execute(q_ultimo_id_item)
  ultimo_id = cursor.fetchone()[0]

  if ultimo_id == None or ultimo_id == 0:
    ultimo_id = 1

  else:
    ultimo_id +=1

  q_id_pedido = 'SELECT max(id_pedido) FROM pedidos'
  cursor.execute(q_id_pedido)
  ultimo_id_pedido = cursor.fetchone()[0]

  q_id_produto = 'SELECT id_produto from produtos'
  cursor.execute(q_id_produto)
  id_produtos = cursor.fetchall()
  id_produto = choice(id_produtos)[0]

  q_quantidade = randint(1,300)

  preco_unitario_produto = 'SELECT preco_unitario FROM itens_pedido where id_produto = %s'
  cursor.execute(preco_unitario_produto,([id_produto]))
  preco_unitario = cursor.fetchone()[0]

  q_inserir_itens_pedidos = 'insert into itens_pedido (id_item, id_pedido, id_produto, quantidade, preco_unitario) ' \
  'values (%s,%s,%s,%s,%s)'

  cursor.execute(q_inserir_itens_pedidos, (ultimo_id, ultimo_id_pedido, id_produto, q_quantidade, preco_unitario))


 conexao.commit()
 cursor.close()
 conexao.close()
