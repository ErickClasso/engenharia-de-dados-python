#!script/env/bin/python3

from utils import escrever_dados_csv, escrever_dados_csv_pandas, escrever_dicios_csv

AnoHoje = 2025

dicionario = {}

dicionario["Nome"] = input("Digite seu nome: ")
dicionario["Sobrenome"] = input("Digite seu sobrenome: ")
dicionario["Email"] = input("Digite seu email: ")
dicionario["Número de Telefone"] = input("Digite seu Número: ")
dicionario["Ano de Nascimento"] = int(input("Digite seu ano de nascimento: "))


dicionario["idade"] = AnoHoje - dicionario["Ano de Nascimento"]
dados_do_cliente = [dicionario]
print(dados_do_cliente)


escrever_dicios_csv(dados=dados_do_cliente)

