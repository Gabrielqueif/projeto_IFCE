import pymysql

# Conexão com o banco de dados
conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123456',
    database='projeto_ifce'
)
name = 'homepage_estados'
# Lista de estados brasileiros com suas siglas
estados = [
    ('Acre', 'AC'),
    ('Alagoas', 'AL'),
    ('Amapá', 'AP'),
    ('Amazonas', 'AM'),
    ('Bahia', 'BA'),
    ('Ceará', 'CE'),
    ('Distrito Federal', 'DF'),
    ('Espírito Santo', 'ES'),
    ('Goiás', 'GO'),
    ('Maranhão', 'MA'),
    ('Mato Grosso', 'MT'),
    ('Mato Grosso do Sul', 'MS'),
    ('Minas Gerais', 'MG'),
    ('Pará', 'PA'),
    ('Paraíba', 'PB'),
    ('Paraná', 'PR'),
    ('Pernambuco', 'PE'),
    ('Piauí', 'PI'),
    ('Rio de Janeiro', 'RJ'),
    ('Rio Grande do Norte', 'RN'),
    ('Rio Grande do Sul', 'RS'),
    ('Rondônia', 'RO'),
    ('Roraima', 'RR'),
    ('Santa Catarina', 'SC'),
    ('São Paulo', 'SP'),
    ('Sergipe', 'SE'),
    ('Tocantins', 'TO')
]

# Cursor
cursor = conexao.cursor()

# Inserir dados na tabela estados
with conexao:
    with conexao.cursor() as cursor:
        # Deletar dados existentes na tabela
        cursor.execute(f'DELETE FROM {name}')
        conexao.commit()
        
        # Inserir novos dados
        for estado in estados:
            cursor.execute(f'INSERT INTO {name} (nome, sigla) VALUES (%s, %s)', estado)
        conexao.commit()

print("Dados inseridos com sucesso!")