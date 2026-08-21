import psycopg2
import os
from dotenv import load_dotenv
from geradores import criacao_tabelas as tab
from dados import dados_produtos as d_prod

conexao = psycopg2.connect(
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password =  os.getenv("DB_PASSWORD"),
    host =  os.getenv("DB_HOST"),
    port =  os.getenv("DB_PORT")
)


print("=== Gerador e Injetor de Dados | Supabase ===")
tab.criar_tabelas()

