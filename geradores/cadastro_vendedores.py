from faker import Faker
from random import choice, triangular
from datetime import date

faker = Faker("pt-BR")

def cadastro_vendedores(qt_vendedores, conexao):  
   cursor = conexao.cursor()
   for i in range(qt_vendedores):
    cursor.execute("SELECT MAX(id_vendedor) FROM vendedores")
    ultimo_id = cursor.fetchone()[0]
    base_id = 0 if ultimo_id is None else ultimo_id
    id_vendedor = base_id + 1
    nome = faker.name()
    equipes = ["Sul", "Norte"]
    equipe = choice(equipes)
    data_contratacao = date.today()
    salario = round(triangular(3000,6500, 3600),2)
    q_inserir_vendedor = "INSERT INTO vendedores (id_vendedor, nome, equipe, data_contratacao, salario) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(q_inserir_vendedor,(id_vendedor,nome,equipe,data_contratacao, salario))
    conexao.commit()
