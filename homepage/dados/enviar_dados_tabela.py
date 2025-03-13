import pandas as pd
import pymysql
import numpy as np

# Conexão com o banco de dados
conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123456',
    database='projeto_ifce'
)

# Cursor
cursor = conexao.cursor()

# Carregar o arquivo Excel
db_estados = pd.read_excel('././arquivos para enviar para db/ise_sinapi_estados.xlsx')

# Substituir valores NaN por None
db_estados = db_estados.replace({np.nan: None})

# Inserir dados na tabela homepage_tabela
with conexao:
    with conexao.cursor() as cursor:
        # Deletar dados existentes na tabela
        cursor.execute('DELETE FROM homepage_tabela')
        conexao.commit()
        
        # Inserir novos dados
        for index, row in db_estados.iterrows():
            cursor.execute('INSERT INTO homepage_tabela (`AC`, `AL`, `AP`, `AM`, `BA`, `CE`, `DF`, `ES`, `GO`, `MA`, `MT`, `MS`, `MG`, `PA`, `PB`, `PR`, `PE`, `PI`, `RJ`, `RN`, `RS`, `RO`, `RR`, `SC`, `SP`, `SE`, `TO`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                           tuple(row))
        conexao.commit()

print("Dados inseridos com sucesso!")