import psycopg2
import os
from dotenv import load_dotenv
from geradores import criacao_tabelas as tab, cadastro_cliente as clien, cadastro_categorias as categ, cadastro_produtos as prod,cadastro_pedido as ped, cadastro_itens_pedidos as itped, cadastro_vendedores as cadv 
from dados.dados_produtos import p_hospitalar, p_eletronicos, p_esportes
from dados.dados_categorias import c_hospitalar, c_eletronicos, c_esportes

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
 print("Gostaria de Criar as tabelas dentro do seu Banco no Supabase?\n1-Sim\n2-Não")
 try:
    escolha = int(input("R: "))
    if escolha == 1:
     tab.criar_tabelas()
     limpar_terminal()
     break
    elif escolha == 2:
     print("Ok!!")
     break
    else:
      print("Selecione uma das opções do menu.")
 except ValueError:
    print("Insira um número inteiro")

while True: # Gera a quantidade Vendedores informada pelo usuário
  print("Quanto vendedores gostaria de gerar?")
  try:
   qt_vendedores = int(input())
   if qt_vendedores < 0:
    print("Insira um número maior que 0")
   else:
    cadv.cadastro_vendedores(qt_vendedores)
    limpar_terminal()
    break
  except ValueError:
    print("Insira um número inteiro")

while True: # Gera a quantidade de Clientes informada pelo usuário
  print("Quantos clientes gostaria de gerar?\n")
  try:
   qt_clientes = int(input())
   if qt_clientes <0:
    print("Insira um número maior que 0")
   else:
    clien.cadastrar_clientes(qt_clientes)
    limpar_terminal()
    break
  except ValueError:
        print("Insira um número inteiro")

while True: # Gera os valores de Categoria e Produtos com base na escolha do usuário
 print("Você gostaria de inserir qual tipo de produtos?\n1 - Produtos Hospitalares\n2 - Produtos Eletrônicos\n3 - Produtos Esportivos\n")
 try:
    escolha_produtos = int(input())
    if escolha_produtos == 1 or escolha_produtos == 2 or escolha_produtos == 3:
      categ.cadastro_categorias(escolha_produtos)
      prod.cadastrar_produtos(escolha_produtos)
      limpar_terminal()
      break
    else:
      print("Selecione uma das opções do menu.")
 except ValueError:
       print("Insira um número inteiro")


