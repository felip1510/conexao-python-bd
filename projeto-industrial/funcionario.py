#agora esse arquivo é um módulo
#responsavel por funcionalidades ref a funcionario

#listar funcionario
from database import conectar

def listar_funcionarios():
        #abrir conexao
        conexao = conectar()
        #criar cursor
        cursor = conexao.cursor()

        #sql da consulta
        sql ="""
        SELECT 
            F.id_funcionario,
            F.nome,
            f.cargo,
            s.nome AS Setor
        from funcionario f
        join setor s on f.id_setor = s.id_setor
        """
        #executa sql
        cursor.execute(sql)

        #recuperar dados
        dados = cursor.fetchall()

        #exibir resultados
        for funcionario in dados:
            print(funcionario)

        #fechar conexao
        cursor.close()
        conexao.close()   

def cadastrar_funcionario(nome, cargo, id_setor):
    conexao = conectar()
    cursor = conexao.cursor()
    conexao.commit()
    sql ="""
    insert into funcionario
        (nome, cargo, id_setor)
    values
    (%s, %s, %s)
    """
    valores = (nome, cargo, id_setor)
    cursor.execute(sql,valores)
    
    print ("funcionario cadastrado")
    cursor.close()
    conexao.close()

def atualizar_cargo(cargo, id_funcionario):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = '''
    update funcinario
    set cargo = %s
    where id_funcionario = %s
    '''
    valores = (cargo, id_funcionario)
    cursor.execute(sql, valores)
    conexao.commit()

    print("funcionario atualizado")

    cursor.close()
    conexao.close()