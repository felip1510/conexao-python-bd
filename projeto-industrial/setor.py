from database import conectar

def listar_setor():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    SELECT 
        id_setor,
        nome,
        localizacao
    FROM setor
    """
    
    cursor.execute(sql)
    
    dados = cursor.fetchall()
    
    for setor in dados: 
        print(setor)

    cursor.close()
    conexao.close()

def criar_setor(nome, localizacao):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO setor (nome, localizacao)
    VALUES (%s, %s)
    """
    valores = (nome, localizacao)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Setor criado com sucesso!")

    cursor.close()
    conexao.close()

def deletar_setor(id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    delete from setor
    where id_setor = %s
    """
    valores = (id_setor)
    cursor.execute(sql, (valores,))
    conexao.commit()

    cursor.close()
    conexao.close()

def atualizar_setor(localizacao, id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE setor
    SET localizacao = %s
    WHERE id_setor = %s
    """
    valores = (localizacao, id_setor)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Setor atualizado com sucesso!")

    cursor.close()
    conexao.close()


def setor_menu():
    while True:
        print("\n====== SISTEMA SETOR ======")
        print("1 - Listar setores")
        print("2 - Cadastrar setor")
        print("3 - Atualizar setor")
        print("4 - Remover setor")
        print("0 - Sair")

        opcao=input("\nEscolha uma opção: ")
        # listar
        if opcao == "1":
            listar_setor()
        # cadastrar
        elif opcao == "2":
            nome = input("nome: ")
            localizacao = input("localização: ")
            criar_setor(nome, localizacao)
        # atualizar
        elif opcao == "3":
            id_setor = input("ID do setor: ")
            localizacao = input("nova_localização: ")
            atualizar_setor(localizacao, id_setor)
        # Deletar
        elif opcao == "4":
            id_setor = input("ID do setor: ")
            deletar_setor(id_setor)
            print("Setor deletado!")
        #Sair
        elif opcao == "0":
            print("Bye Bye")
            break
        else:
            print("Tente novamente!")