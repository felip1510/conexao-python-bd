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
        print(funcionario)

    #fechar a conexao

    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome, cpf, cargo, salario, data_admissao, id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO funcionario (nome, cpf, cargo, salario, data_admissao, id_setor)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (nome, cpf, cargo, salario, data_admissao, id_setor)
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
    DELETE FROM funcionario
    WHERE id_funcionario = %s
    """
    valores = (id_funcionario)
    cursor.execute(sql, (valores,))
    conexao.commit()

    cursor.close()
    conexao.close()

def funcionario_menu():
    while True:
        print("\n====== SISTEMA FUNCIONARIO ======")
        print("1 - Listar funcionários")
        print("2 - Cadastrar funcionário")
        print("3 - Atualizar cargo")
        print("4 - Remover funcionário")
        print("0 - Sair")

        opcao=input("\nEscolha uma opção: ")
        # listar
        if opcao == "1":
            listar_funcionarios()
        # cadastrar
        elif opcao == "2":
            nome = input("nome: ")
            cpf = input("cpf: ")
            cargo = input("cargo: ")
            salario = float(input("salario: "))
            data_admissao = input("data de admissao (AAAA-MM-DD): ")
            id_setor = int(input("ID setor: "))
            cadastrar_funcionario(nome, cpf, cargo ,salario ,data_admissao, id_setor)
            print("Funcionario cadastrado com sucesso!")
        # atualizar
        elif opcao == "3":
            id_funcionario = input("ID do funcionario: ")
            novo_cargo = input("Cargo: ")
            atualizar_cargo(id_funcionario,novo_cargo)
            print("Cargo atualizado!")
        # Deletar
        elif opcao == "4":
            id_funcionario = input("ID do funcionario: ")
            deletar_funcionario(id_funcionario)
            print("Funcionario deletado!")
        #Sair
        elif opcao == "0":
            print("Bye Bye")
            break
        else:
            print("Tente novamente!")