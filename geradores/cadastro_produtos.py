import psycopg2
import os
from dotenv import load_dotenv 
import random
from dados.dados_produtos import p_hospitalar, p_eletronicos, p_esportes

load_dotenv()
conexao = psycopg2.connect(
     dbname = os.getenv("DB_NAME"),
     user = os.getenv("DB_USER"),
     password = os.getenv("DB_PASSWORD"),
     host = os.getenv("DB_HOST"),
     port = os.getenv("DB_PORT")
)



def cadastrar_produtos(lista):
 while True:
  cursor = conexao.cursor()
  cursor.execute("SELECT MAX(id_produto) FROM produtos")
  ultimo_id = cursor.fetchone()[0]
  base_id = 0 if ultimo_id is None else ultimo_id
  try:
   print("Você gostaria de inserir qual tipo de produtos?\n1 - Produtos Hospitalares\n2 - Produtos Eletrônicos\n3 - Produtos Esportivos")
   escolha_produtos = int(input())
   if escolha_produtos == 1:
    dados_produtos = lista[0]
    break
   elif escolha_produtos == 2:
    dados_produtos = lista[1]
    break
   elif escolha_produtos == 3:
    dados_produtos = lista[3]
    break
   else:
    print("Informe o número das opções acima")
  
  except ValueError:
   print("Informe um número")
  qt_produtos = len(dados_produtos)
  for i in range(qt_produtos):
   id_produto = base_id + 1 + i
   nome_produto = dados_produtos[i][0]
   id_categoria = dados_produtos[i][1]
   preco = dados_produtos[i][2]
   estoque = random.randint(1,300)
  q_inserir_produtos = "INSERT into produtos(id_produto, nome_produto, id_categoria, preco, estoque) VALUES (%s,%s,%s,%s,%s)" 
  cursor.execute(q_inserir_produtos, (id_produto, nome_produto, id_categoria, preco, estoque))

 conexao.commit()
 cursor.close()
 conexao.close() 
