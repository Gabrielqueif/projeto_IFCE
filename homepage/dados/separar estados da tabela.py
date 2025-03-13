import pandas as pd
import pymysql

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
db = pd.read_excel('././arquivos para enviar para db/ise sinapi.xlsx')

# Lista de siglas dos estados
siglas_estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

# Selecionar apenas as colunas dos estados
db_estados = db[siglas_estados]

# Salvar o resultado em um novo arquivo Excel
db_estados.to_excel('././arquivos para enviar para db/ise_sinapi_estados.xlsx', index=False)

print("Arquivo Excel limpo e salvo com sucesso!")
