import psycopg2
import os
from dotenv import load_dotenv
from geradores import criacao_tabelas as tab, cadastro_cliente as clien, cadastro_categorias as categ, cadastro_produtos as prod,cadastro_pedido as ped, cadastro_itens_pedidos as itped, cadastro_vendedores as cadv 
from dados.dados_produtos import p_hospitalar, p_eletronicos, p_esportes
from dados.dados_categorias import c_hospitalar, c_eletronicos, c_esportes
from random import randint

load_dotenv()
conexao = psycopg2.connect(
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password =  os.getenv("DB_PASSWORD"),
    host =  os.getenv("DB_HOST"),
    port =  os.getenv("DB_PORT")
)

def limpar_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')
print("=== Gerador e Injetor de Dados | Supabase ===\n")

while True: # Cria as tabelas de Clientes, Categorias, Produtos, Vendedores, Pedidos e Itens_Pedidos.
 print("Preencher Banco de dados Supabase:\n1 - Manualmente\n2 - Automaticamente")
 try:
    escolha = int(input("R: "))
    if escolha == 1 or escolha ==2:
     tab.criar_tabelas(conexao)
     limpar_terminal()
     break
    else:
      print("Selecione uma das opções do menu.")
 except ValueError:
    print("Insira um número inteiro")

while True: # Gera a quantidade Vendedores informada pelo usuário
 if escolha == 1:
  print("Quanto vendedores gostaria de gerar?")
  try:
   qt_vendedores = int(input())
   if qt_vendedores < 0:
     print("Insira um número maior que 0")
   else:
     cadv.cadastro_vendedores(qt_vendedores, conexao)
     limpar_terminal()
     break
  except ValueError:
      print("Insira um número inteiro")
 else:
     cadv.cadastro_vendedores(5, conexao)
     limpar_terminal()
     break
  
while True: # Gera a quantidade de Clientes informada pelo usuário
 if escolha == 1:
  print("Quantos clientes gostaria de gerar?\n")
  try:
   qt_clientes = int(input())
   if qt_clientes <0:
     print("Insira um número maior que 0")
   else:
     clien.cadastrar_clientes(qt_clientes, conexao)
     limpar_terminal()
     break
  except ValueError:
           print("Insira um número inteiro")
 else:
      clien.cadastrar_clientes(18, conexao)
      limpar_terminal()
      break
  
while True: # Gera os valores de Categoria e Produtos com base na escolha do usuário
 if escolha == 1:
  print("Você gostaria de inserir qual tipo de produtos?\n1 - Produtos Hospitalares\n2 - Produtos Eletrônicos\n3 - Produtos Esportivos\n")
  try:
    escolha_produtos = int(input())
    if escolha_produtos == 1 or escolha_produtos == 2 or escolha_produtos == 3:
       categ.cadastro_categorias(escolha_produtos, conexao)
       prod.cadastrar_produtos(escolha_produtos, conexao)
       limpar_terminal()
       break
    else:
       print("Selecione uma das opções do menu.")
  except ValueError:
    print("Insira um número inteiro")
 else:
      escolha_produtos = randint(1,3)
      categ.cadastro_categorias(escolha_produtos, conexao)
      prod.cadastrar_produtos(escolha_produtos, conexao)
      limpar_terminal()
      break
  
while True:# Gera os pedidos de venda
 if escolha == 1:
  print("Quantos pedidos deseja informar?")
  try:
    qt_pedidos = int(input())
    if qt_pedidos < 0:
       print("Insira um número maior que 0")
    else:
       for i in range(qt_pedidos):
        id_pedido = ped.criar_pedidos()
        itped.cadastrar_itens_pedido(id_pedido, conexao)
        limpar_terminal()
       break
  except ValueError:
    print("Insira um número")
 else:
      for i in range(1,43):
        id_pedido = ped.criar_pedidos(conexao)
        itped.cadastrar_itens_pedido(id_pedido, conexao)
        limpar_terminal()
      break

cursor = conexao.cursor()
cursor.close()
conexao.close()