import pymysql
import pandas as pd

# Carregar os dados
tabela = pd.read_excel('arquivos para enviar para db/ise sinapi.xlsx')

# Renomear a coluna no DataFrame para coincidir com o nome no banco de dados
tabela.rename(columns={'Origem de Preço': 'Origem_de_Preço'}, inplace=True)

# Conectar ao banco
conection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='projeto_ifce',
)
table_name = 'insumos'

with conection:
    with conection.cursor() as cursor:
        # Criar a tabela garantindo que os nomes sejam iguais
        cursor.execute(
            f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                classificação TEXT NOT NULL,
                Codigo_do_insumo INTEGER NOT NULL,
                descrição_do_insumo LONGTEXT NOT NULL,
                Unidade TEXT,
                Origem_de_Preço TEXT,  -- Nome ajustado para evitar espaços
                PRIMARY KEY (Codigo_do_insumo)
            )
            '''
        )
        conection.commit()
        print('Conexão bem-sucedida')

    with conection.cursor() as cursor:
        # Criar a lista de dados para inserção
        dados_lista = [
            (
                tabela['Classificação'][n],
                tabela['Código do Insumo'][n],
                tabela['Descrição do Insumo'][n],
                tabela['Unidade'][n],
                tabela['Origem_de_Preço'][n]  # Nome corrigido no DataFrame
            )
            for n in tabela.index
        ]
        # comando para inserir os dados na base de dados
        # %s é um placeholder que serve para pegar os dados que são informados mais acima

        sql = (
            f'INSERT INTO {table_name} '
            '(classificação, Codigo_do_insumo, descrição_do_insumo, Unidade, Origem_de_Preço) '
            'VALUES (%s, %s, %s, %s, %s)'
        )
        # faço a execução do comando sql com os dados que são gerados
        cursor.executemany(sql, dados_lista)
        conection.commit()
