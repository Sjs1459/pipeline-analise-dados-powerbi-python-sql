from datetime import date
from random import choice
from ibge.localidades import Estados, Municipios
from faker import Faker

fake = Faker('pt-BR')

estados = Estados().json()
municipios = Municipios().json()
def cadastrar_clientes(qt_clientes, conexao): 
 cursor = conexao.cursor()
 q_ultimo_id_cliente = 'SELECT max(id_cliente) FROM clientes'
 cursor.execute(q_ultimo_id_cliente)
 ultimo_id_cliente = cursor.fetchone()[0]
 base_id = 0 if ultimo_id_cliente is None else ultimo_id_cliente
 for i in range(qt_clientes):
  id_cliente = base_id + 1 + i
  nome = fake.company()
  cidade = choice(municipios)
  nome_cidade = cidade['nome']
  estado = cidade['microrregiao']["mesorregiao"]['UF']['sigla']
  email = fake.company_email()
  data = date.today()
  ativo = choice([True, False])

  query_inserir_cliente = "insert into clientes (id_cliente, nome, cidade,estado, email, data_cadastro,ativo) " \
  "values (%s, %s, %s, %s, %s, %s, %s)"
  cursor.execute(query_inserir_cliente, (id_cliente, nome, nome_cidade,estado, email, data, ativo))
 conexao.commit()



