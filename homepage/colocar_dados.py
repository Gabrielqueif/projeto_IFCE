import pandas as pd
import pymysql

# Conexão com o banco de dados
conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123456',
    database='projeto_ifce'
)
NAME = 'homepage_insumos'
# Cursor
cursor = conexao.cursor()
db = pd.read_excel('./arquivos para enviar para db/ise sinapi.xlsx')
#print(db)
with conexao:
    with conexao.cursor() as cursor:
        for i in range(len(db)):
            cursor.execute(f'INSERT INTO {NAME} (Classificação, codigo_insumo, descrição_insumo, unidade, origem_preço) VALUES (%s, %s, %s, %s, %s)', (db['Classificação'][i], db['Código do Insumo'][i], db['Descrição do Insumo'][i], db['Unidade'][i], db['Origem de Preço'][i]))
            conexao.commit()

