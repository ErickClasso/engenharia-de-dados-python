#!script/env/bin/python3


# 1 - importar função que escreve dados
from utils import escrever_dados_csv, escrever_dados_csv_pandas
# 2 - salvar uma lista temporaria
# 3 - escrever dados no arquivo csv

# nome = "Fabio"
dados_clientes = []

# input de dados dinamicos
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
telefone = input("Telefone: ")
email = input("Email: ")
print(f"Você digitou 'Nome'== {nome}")
print(f"Você digitou 'Sobrenome'== {sobrenome}")
print(f"Você digitou 'Telefone'== {telefone}")
print(f"Você digitou 'Email'== {email}")
dados_clientes.append(nome)
dados_clientes.append(sobrenome)
dados_clientes.append(telefone)
dados_clientes.append(email)
print(f"Confirma os dads: {dados_clientes}")

#escrever_dados_csv(dados=dados_clientes)
escrever_dados_csv_pandas(dados=dados_clientes)

# Desafio passar um dicionario de parametros para dentro da lista