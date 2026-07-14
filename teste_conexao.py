from database import conectar

def relatorio_producao_por_setor():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT 
    s.nome AS setor,
    sum(o.quantidade_produzida) AS total_produtos
    FROM setor s
    JOIN funcionario f
    ON f.id_setor = s.id_setor
    JOIN ordem_producao o
    ON o.id_funcionario = f.id_funcionario
    GROUP BY s.nome
    order by total_produtos desc
    """
    cursor.execute(sql)
    dados = cursor.fetchall()

    print("\n ----- Produção por setor -----")

    for relatorio in dados:
        print(f"\nSetor: {relatorio[0]}")
        print(f"\nTotal Produzido: {relatorio[1]}")
        print("-" * 40)

    cursor.close()
    conexao.close()