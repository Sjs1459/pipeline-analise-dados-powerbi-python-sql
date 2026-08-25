def criar_tabelas(conexao):
 cursor = conexao.cursor()
 cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
id_cliente int PRIMARY KEY,
nome varchar(100),
cidade varchar(100),
estado varchar(2),
email varchar(100),
data_cadastro date,
ativo boolean
);

CREATE TABLE IF NOT EXISTS vendedores(
id_vendedor int PRIMARY KEY,
nome varchar(100),
equipe varchar(50),
data_contratacao date,
salario numeric
);

CREATE TABLE IF NOT EXISTS pedidos(
id_pedido int PRIMARY KEY,
id_cliente int,
id_vendedor int,
data_pedido date,
status varchar(50),
FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
FOREIGN KEY(id_vendedor) REFERENCES vendedores(id_vendedor));

CREATE TABLE IF NOT EXISTS categorias(
id_categoria int PRIMARY KEY,
nome_categoria varchar(50));

CREATE TABLE IF NOT EXISTS produtos(
id_produto int PRIMARY KEY,
nome_produto varchar(50),
id_categoria int, 
preco NUMERIC(50),
estoque int,
FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria));

CREATE TABLE IF NOT EXISTS itens_pedido(
id_item int PRIMARY KEY,
id_pedido int,
id_produto int,
quantidade int,
preco_unitario NUMERIC,
FOREIGN KEY(id_pedido) REFERENCES pedidos(id_pedido));""")

 conexao.commit()



