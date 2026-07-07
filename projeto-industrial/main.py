from funcionario import funcionario_menu
from setor import setor_menu

#listar_funcionarios()
#cadastrar_funcionario("testeman", "12345678910","testador",6000.00,"2025-02-03",1)
#tualizar_cargo( 1,"tecnico")
#deletar_funcionario(3)


#listar_setor()
#criar_setor("Pintura", 'Bloco E')
#deletar_setor(7)
#atualizar_setor('Bloco C',2)

while True:
    print("-------Menu Geral-------")
    print("Funcionario_menu = 1")
    print("Setor_menu = 2")
    print("Sair = 0")
    print("---------------------")
    opcao = int(input("Selecione qual opção deseja: "))

    if opcao == 1:
        funcionario_menu()
    elif opcao == 2:
        setor_menu()
    elif opcao == 0:
        print("Tchau!")
        break
    else:
        print("erro")
