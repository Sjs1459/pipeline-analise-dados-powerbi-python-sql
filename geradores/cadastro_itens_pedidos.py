import psycopg2
import os
from random import randint, choice
from dotenv import load_dotenv
from dados.dados_produtos import p_eletronicos,p_esportes,p_hospitalar
from geradores import cadastro_pedido as ped

load_dotenv()

conexao = psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"))

cursor = conexao.cursor()

def cadastrar_itens_pedido(id_pedido):
   for j in range(randint(1,3)):
    q_ultimo_id_item = 'SELECT MAX(id_item) FROM itens_pedido' #Seleciona o ultimo id_item para somar e descobrir o próximo, construindo em sequência
    cursor.execute(q_ultimo_id_item)
    ultimo_id = cursor.fetchone()[0]
    ultimo_id = 0 if ultimo_id is None else ultimo_id
    id_item = ultimo_id + 1 

    q_id_produto = 'SELECT id_produto FROM produtos' # Seleciona produtos aleatórios para os pedidos
    cursor.execute(q_id_produto)
    id_produtos = cursor.fetchall()
    id_produto = choice(id_produtos)[0]

    q_quantidade = "SELECT estoque FROM produtos WHERE id_produto = %s" # Verifica quanto que tem no estoque e faz itens pedidos com base nisso
    cursor.execute(q_quantidade, (id_produto,))
    quantidade_total = cursor.fetchone()[0]
    quantidade = randint(1, quantidade_total)

    preco_unitario_produto = 'SELECT preco FROM produtos WHERE id_produto = %s' # Pega o preço unitario do produto correto
    cursor.execute(preco_unitario_produto,(id_produto,))
    preco_unitario = cursor.fetchone()[0]

    q_inserir_itens_pedidos = 'INSERT INTO itens_pedido (id_item, id_pedido, id_produto, quantidade, preco_unitario) ' \
    'VALUES (%s,%s,%s,%s,%s)'
    cursor.execute(q_inserir_itens_pedidos, (id_item, id_pedido, id_produto, quantidade, preco_unitario))
    conexao.commit()

