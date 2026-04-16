import pandas as pd

df = pd.read_csv('data/train.csv')

# passo 6.1 tratamento das colunas
# renomeação das colunas para snake_case
mapeamento_colunas = {
    'PassengerId': 'id_passageiro',
    'Survived': 'sobreviveu',
    'Pclass': 'classe_pax',
    'Name': 'nome',
    'Sex': 'sexo',
    'Age': 'idade',
    'SibSp': 'irmaos_conjuges',
    'Parch': 'pais_filhos',
    'Ticket': 'bilhete',
    'Fare': 'tarifa',
    'Cabin': 'cabine',
    'Embarked': 'porto_embarque'
}

df.rename(columns=mapeamento_colunas, inplace=True)

colunas_categoricas = ['sexo', 'porto_embarque', 'classe_pax', 'sobreviveu']

for coluna in colunas_categoricas:
    df[coluna] = df[coluna].astype('category')

print(df.info())

# passo 6.2 tratamento de nulos

df['cabine'] = df['cabine'].fillna('Nao_Informado')

moda_porto = df['porto_embarque'].mode()[0]

df['porto_embarque'] = df['porto_embarque'].fillna(moda_porto)

df['idade'] = df['idade'].fillna(
    df.groupby(['classe_pax', 'sexo'])['idade'].transform('median')
)


print("\n--- Contagem de valores nulos após o tratamento ---")
print(df.isnull().sum())