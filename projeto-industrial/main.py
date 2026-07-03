from funcionario import listar_funcionarios
from funcionario import cadastrar_funcionario
from funcionario import atualizar_cargo
from funcionario import deletar_funcionario
from setor import listar_setor
from setor import criar_setor
from setor import deletar_setor
from setor import atualizar_setor

#listar_funcionarios()
#cadastrar_funcionario("testeman", "12345678910","testador",6000.00,"2025-02-03",1)
#tualizar_cargo( 1,"tecnico")
#deletar_funcionario(3)


#listar_setor()
#criar_setor("Pintura", 'Bloco E')
#deletar_setor(7)
#atualizar_setor('Bloco C',2)

while True:
    print("\n====== SISTEMA INDUSTRIAL ======")
    print("1 - Listar funcionários")
    print("2 - Cadastrar funcionário")
    print("3 - Atualizar salário")
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
        salario = input("salario: ")
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
