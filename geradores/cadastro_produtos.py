from random import randint
from dados.dados_produtos import p_hospitalar, p_eletronicos, p_esportes

def cadastrar_produtos(escolha_produtos, conexao):
  tipos_produtos = [p_hospitalar, p_esportes,p_eletronicos]
  dados_produtos = tipos_produtos[escolha_produtos-1]
  qt_produtos = len(dados_produtos)
  for i in range(qt_produtos):
   cursor = conexao.cursor()
   cursor.execute("SELECT MAX(id_produto) FROM produtos")
   ultimo_id = cursor.fetchone()[0]
   base_id = 0 if ultimo_id is None else ultimo_id
   id_produto = base_id + 1 
   nome_produto = dados_produtos[i][0]
   id_categoria = dados_produtos[i][1]
   preco = dados_produtos[i][2]
   estoque = randint(1,300)
   q_inserir_produtos = "INSERT into produtos(id_produto, nome_produto, id_categoria, preco, estoque) VALUES (%s,%s,%s,%s,%s)" 
   cursor.execute(q_inserir_produtos, (id_produto, nome_produto, id_categoria, preco, estoque))
   conexao.commit()
   

