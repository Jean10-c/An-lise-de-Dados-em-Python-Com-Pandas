import pandas as pd

# Leitura do arquivo CSV
dados = pd.read_csv(
    "dados.csv",
    sep=";",
    engine="python",
    encoding="utf-8"
)

# Informações gerais
print("=== INFORMAÇÕES GERAIS ===")
print(dados.info())

# Primeiras e últimas 5 linhas
print("\n=== PRIMEIRAS 5 LINHAS ===")
print(dados.head())

print("\n=== ÚLTIMAS 5 LINHAS ===")
print(dados.tail())

# Cria uma cópia do DataFrame original
dados_tratados = dados.copy()

# Substitui valores nulos de Calories por 0
dados_tratados["Calories"] = dados_tratados["Calories"].fillna(0)

print("\n=== APÓS SUBSTITUIR NaN DE CALORIES POR 0 ===")
print(dados_tratados)

# Substitui valores nulos de Date por 1900/01/01
dados_tratados["Date"] = dados_tratados["Date"].fillna("1900/01/01")

print("\n=== APÓS SUBSTITUIR NaN DE DATE ===")
print(dados_tratados)

# Corrige o valor 20201226
dados_tratados["Date"] = dados_tratados["Date"].replace(
    "20201226",
    "'2020/12/26'"
)

# Remove o valor fictício criado anteriormente
dados_tratados["Date"] = dados_tratados["Date"].replace(
    "1900/01/01",
    pd.NA
)

# Converte a coluna Date para datetime
dados_tratados["Date"] = pd.to_datetime(
    dados_tratados["Date"],
    format="'%Y/%m/%d'",
    errors="coerce"
)

print("\n=== APÓS CONVERSÃO PARA DATETIME ===")
print(dados_tratados)

# Remove linhas com valores nulos
dados_tratados = dados_tratados.dropna()

print("\n=== DATAFRAME FINAL ===")
print(dados_tratados)

print("\n=== INFORMAÇÕES FINAIS ===")
print(dados_tratados.info())