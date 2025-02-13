import os
import django
import pandas as pd
# Certifique-se de que o caminho está correto
from models import insumos
from project import settings

# Configuração do Django
settings.configure()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

# Caminho para o arquivo Excel
excel_file = 'arquivos para enviar para db/ise sinapi.xlsx'

# Leia o arquivo Excel
df = pd.read_excel(excel_file)

# Itere sobre as linhas do DataFrame e insira os dados no banco de dados
for index, row in df.iterrows():
    uploaded_file = insumos(
        material=row['classificação'],
        codigo=row['Codigo_do_insumo'],
        descricao=row['descricao_do_insumo'],
        unidade=row['Unidade'],
        origem_preco=row['Origem_de_preco'],

    )
    uploaded_file.save()
