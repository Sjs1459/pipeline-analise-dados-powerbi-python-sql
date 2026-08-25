from dados.dados_categorias import c_hospitalar, c_esportes, c_eletronicos

def cadastro_categorias(escolha_produtos, conexao):
  tipos_categorias = [c_hospitalar,c_esportes,c_eletronicos]
  dados_produtos = tipos_categorias[escolha_produtos-1]
  qt_categorias = len(dados_produtos)
  cursor = conexao.cursor()
  q_inserir_categorias = "INSERT INTO categorias (id_categoria, nome_categoria) values (%s, %s)"
  id_categoria = 0
  for i in range(qt_categorias):
   id_categoria +=1
   nome = dados_produtos[i]
   cursor.execute(q_inserir_categorias,(id_categoria, nome))
   conexao.commit()
 
  

