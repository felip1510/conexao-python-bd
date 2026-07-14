from database import conectar

#-------------------------------------------------------------------------------------------

def listar_produto():
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT 
                id_produto,
                nome,
                descricao,
                preco_fabricacao,
                quantidade_estoque,
                c.nome as categoria,
                f.razao_social as fornecedor

            FROM produto p
            JOIN categoria c ON p.id_categoria = c.id_categoria
            JOIN fornecedor f ON p.id_fornecedor = f.id_fornecedor
            on f.id_fornecedor = p.id_fornecedor
            """
        cursor.execute(sql)
        dados = cursor.fetchall()

        for produto in dados: 
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Preço de Fabricação: {produto[2]}")
            print(f"Quantidade em Estoque: {produto[3]}")
            print(f"Categoria: {produto[4]}")
            print(f"Fornecedor: {produto[5]}")
            print("-" * 40)

    
        cursor.close()
        conexao.close()

#-------------------------------------------------------------------------------------------
def cadastrar_produto(nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria , id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO produto ( nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria , id_fornecedor)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = ( nome, descricao, preco_fabricacao, quantidade_estoque, id_categoria , id_fornecedor )
    cursor.execute(sql, valores)
    conexao.commit()

    print("Produto cadastrado com sucesso!")

    cursor.close()
    conexao.close()
    
#-------------------------------------------------------------------------------------------

def atualizar_produto(id_produto, novo_nome):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE produto
    SET nome = %s
    WHERE id_fproduto = %s
    """
    valores = (novo_nome, id_produto)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Produto atualizado com sucesso!")

    cursor.close()
    conexao.close()
    
#-------------------------------------------------------------------------------------------

def remover_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = """
    delete from produto
    where id_produto = %s
    """
    valores = (id_produto)
    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

#-------------------------------------------------------------------------------------------

def buscar_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT 
        id_produto,
        nome,
        descricao,
        preco_fabricacao,
        quantidade_estoque,
        id_categoria ,
        id_fornecedor

    FROM produto
    WHERE id_produto = %s
    """
    cursor.execute(sql, (id_produto,))
    produto = cursor.fetchone()

    if produto:
        print(produto)
    else:
        print("Produto não encontrado.")

    cursor.close()
    conexao.close()