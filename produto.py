#AGORA ESSE ARQUIVO É UM MÓDULO
#RESPONSÁVEL POR FUNCIONALIDADES REFERENTES A FUNCIONÁRIO

#listar conexão
from database import conectar


def listar_funcionarios():
#Abrir conexão
    conexao = conectar()

    #Criar cursor

    cursor = conexao.cursor()

    #sql da consulta

    sql = """
    SELECT 
        f.id_funcionario,
        f.nome,
        f.cpf,
        f.cargo,
        f.salario,
        f.data_admissao,
        s.nome AS setor
    from funcionario f
    join setor s on f.id_setor = s.id_setor
    """
    #executa sql
    cursor.execute(sql)

    #recuperar dados
    dados = cursor.fetchall()


    #exibir dados
    for funcionario in dados: 
        print(f"ID: {funcionario[0]}")
        print(f"Nome: {funcionario[1]}")
        print(f"Cargo: {funcionario[2]}")
        print(f"Setor: {funcionario[3]}")
        print("-" * 40)

    #fechar a conexao

    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome,cpf,cargo,salario,data_admissao,id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO funcionario (nome,cpf,cargo,salario,data_admissao,id_setor)
    VALUES (%s, %s, %s,%s, %s, %s)
    """
    valores = (nome,cpf,cargo,salario,data_admissao,id_setor)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Funcionário cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_cargo(id_funcionario, novo_cargo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE funcionario
    SET cargo = %s
    WHERE id_funcionario = %s
    """
    valores = (novo_cargo, id_funcionario)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Cargo do funcionário atualizado com sucesso!")

    cursor.close()
    conexao.close()
    
def deletar_funcionario(id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    delete from funcionario
    where id_funcionario = %s
    """
    valores = (id_funcionario)
    cursor.execute(sql, (valores,))
    conexao.commit()
    print("Funcionário removido com sucesso!")

    cursor.close()
    conexao.close()


    cursor.close()
    conexao.close()

def buscar_funcionario(id_funcionario):
        try:
            conexao = conectar()
            cursor = conexao.cursor()

            sql = """
            SELECT 
                f.id_funcionario,
                f.nome,
                s.nome AS setor
            from funcionario f
            join setor s on f.id_setor = s.id_setor
            where f.id_funcionario = %s
            """
            valores = (id_funcionario,)
            cursor.execute(sql, valores)

            funcionario = cursor.fetchone()

            if funcionario:
                print(f"ID: {funcionario[0]}")
                print(f"Nome: {funcionario[1]}")
                print(f"Setor: {funcionario[2]}")
            else:
                print("Funcionário não encontrado.")

            cursor.close()
            conexao.close()
        except Exception as erro:
            print(erro)