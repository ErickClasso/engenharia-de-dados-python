#!script/env/bin/python3

import csv

def escrever_dados_csv(dados):
    with open('cadastro_clientes.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dados)
    return f"Dados salvos com sucesso!"


# Utilizando pandas
# Instalar pandas com: pip install pandas
import pandas as pd # aliases de pandas

def escrever_dados_csv_pandas(dados):
    df = pd.DataFrame([dados], columns=['Nome', 'Sobrenome', 'Telefone', 'Email'])
    df.to_csv('cadastro_clientes_2.csv', mode='a', header=False, index=False)
    return f"Dados salvos com sucesso!"

def escrever_dicios_csv(dados):
    with open('cadastro_clientes_novo.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dados)
    return f"Dados salvos com sucesso!"

