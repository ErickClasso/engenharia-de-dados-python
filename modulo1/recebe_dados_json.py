import json

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
telefone = input("Telefone: ")
email = input("Email: ")

data = {}
data['nome'] = str(nome).lower()
data['sobrenome'] = str(sobrenome).lower()
data['telefone'] = telefone
data['email'] = email

def _recebe_dados_json(dados_do_cliente):
    nome_do_cliente = nome + sobrenome
    with open(f'clientes2025.json', 'w') as file:  # w = writer, a = append
        json.dump(data, file, indent=4)

_recebe_dados_json(dados_do_cliente=data)

# criar um arquivo geral com os dados de todos juntos no mesmo arquivo