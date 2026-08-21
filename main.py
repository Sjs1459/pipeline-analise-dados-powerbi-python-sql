import psycopg2
import os
from dotenv import load_dotenv
from geradores import criacao_tabelas as tab, cadastro_cliente as clien, cadastro_categorias as categ, cadastro_produtos as prod,cadastro_pedido as ped, cadastro_itens_pedidos as itped 
from dados import dados_produtos as d_prod

conexao = psycopg2.connect(
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password =  os.getenv("DB_PASSWORD"),
    host =  os.getenv("DB_HOST"),
    port =  os.getenv("DB_PORT")
)


print("=== Gerador e Injetor de Dados | Supabase ===\n")
while True: 
 print("Gostaria de Criar as tabelas dentro do seu Banco no Supabase?\n1-Sim\n2-Não")
 try:
    escolha = int(input(""))
    if escolha == 1:
     tab.criar_tabelas
    elif escolha == 2:
     print("Ok!!")
    else:
      print("Insira um número de uma das opções")
 except ValueError:
   print("Insira um número")


