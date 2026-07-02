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
