from funcionario import(
listar_funcionarios,
deletar_funcionario,
cadastrar_funcionario,
atualizar_cargo,
buscar_funcionario,
)

from produto import(
listar_produto,
)

from relatorios import(
relatorio_producao_por_setor,
)

while True:

    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar funcionários")
    print("2 - Cadastrar funcionário")
    print("3 - Atualizar salário")
    print("4 - Remover funcionário")
    print("5 - Buscar funcionário")
    print("6 - Listar produtos")
    print("7 - Relatório de produção por setor")
    print("0 - Sair")

    opcao=input("\nEscolha uma opção: ")
    # listar
    if opcao == "1":
        listar_funcionarios()
    #CADASTRAR
    elif opcao=="2":
        nome = input("Nome:")
        cpf = input("CPF:")
        cargo = input("Cargo:")
        salario = float(input("Salario: "))
        data_admissao = input("Data de admissão(AAAA-MM-DD):")
        id_setor = int(input("ID setor:"))

        cadastrar_funcionario(nome,cpf,cargo,salario,data_admissao,id_setor)
        print("Funcionário cadastrado com sucesso!")
    #ATUALIZAR
    elif opcao == "3":
        id_funcionario = input("ID funcionario:")
        novo_cargo = input("Cargo:")

        atualizar_cargo(id_funcionario,novo_cargo)
    #DELETAR
    elif opcao == "4":
        id_funcionario = input("ID funcionario:")

        deletar_funcionario(id_funcionario)
    #BUSCAR
    elif opcao == "5":
        id_funcionario = input("ID funcionario: ")
        buscar_funcionario(id_funcionario)
    #Listar produtos
    elif opcao == "6":
        listar_produto()
    # Relatório de produção por setor
    elif opcao == "7":
        relatorio_producao_por_setor()
    #SAIR
    elif opcao=="0":
        print("bye bye")
        break
    else:
        print("Tente novamente!!!!!!!!!!!!!!")



