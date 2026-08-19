import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
conexao = psycopg2.connect(
       dbname = os.getenv('DB_NAME'),
       user = os.getenv('DB_USER'),
       password = os.getenv('DB_PASSWORD'),
       host = os.getenv('DB_HOST'),
       port = os.getenv('DB_PORT')
)

cursor = conexao.cursor('')

cursor.execute()


cursor.close()
conexao.close()