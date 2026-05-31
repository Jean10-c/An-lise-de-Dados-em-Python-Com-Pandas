import pandas as pd

# Microatividade 1
dados = pd.read_csv(
    "dados.csv",
    sep=";",
    engine="python",
    encoding="utf-8"
)

print("CONJUNTO ORIGINAL:")
print(dados)

# Microatividade 2
subconjunto = dados[["Duration", "Pulse", "Calories"]]

print("\nSUBCONJUNTO:")
print(subconjunto)

# Microatividade 3
pd.set_option("display.max_rows", 9999)

print("\nCONJUNTO COMPLETO:")
print(dados.to_string())

# Exibe as 10 primeiras linhas
print("PRIMEIRAS 10 LINHAS:")
print(dados.head(10))

# Exibe as 10 últimas linhas
print("\nÚLTIMAS 10 LINHAS:")
print(dados.tail(10))

# Informações gerais do DataFrame
print(dados.info())