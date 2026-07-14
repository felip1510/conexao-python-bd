from database import conectar

#-------------------------------------------------------------------------------------------

def listar_fornecedor():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT 
        id_fornecedor,
        cnpj,
        telefone,
        cidade

    FROM fornecedor
    """
    cursor.execute(sql)
    dados = cursor.fetchall()

    for fornecedor in dados: 
        print(fornecedor)
    cursor.close()
    conexao.close()

#-------------------------------------------------------------------------------------------
def cadastrar_fornecedor(cnpj,telefone, cidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO fornecedor ( cnpj, telefone, cidade)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = ( cnpj, telefone, cidade )
    cursor.execute(sql, valores)
    conexao.commit()

    print("Fornecedor cadastrado com sucesso!")

    cursor.close()
    conexao.close()
    
#-------------------------------------------------------------------------------------------

def atualizar_cidade(id_fornecedor, nova_cidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE fornecedor
    SET cidade = %s
    WHERE id_fornecedor = %s
    """
    valores = (nova_cidade, id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Cidade do fornecedor atualizado com sucesso!")

    cursor.close()
    conexao.close()
    
#-------------------------------------------------------------------------------------------

def remover_fornecedor(id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()
    
    sql = """
    delete from fornecedor
    where id_fornecedor = %s
    """
    valores = (id_fornecedor)
    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
   
#-------------------------------------------------------------------------------------------

def buscar_fornecedor(id_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT 
        id_fornecedor,
        cnpj,
        telefone,
        cidade

    FROM fornecedor
    WHERE id_fornecedor = %s
    """
    cursor.execute(sql, (id_fornecedor,))
    dados = cursor.fetchall()

    for fornecedor in dados: 
        print(fornecedor)
    cursor.close()
    conexao.close()