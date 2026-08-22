import psycopg2
import os
from dotenv import load_dotenv
from faker import Faker

load_dotenv()

conexao = psycopg2.connect(
     dbname = os.getenv("DB_NAME"),
     user = os.getenv("DB_USER"),
     password = os.getenv("DB_PASSWORD"),
     host = os.getenv("DB_HOST"),
     port = os.getenv("DB_PORT")
)

def cadastro_vendedores():
    