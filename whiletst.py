import json

while True:
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    data = {}
    data['nome'] = str(nome).lower()
    data['sobrenome'] = str(sobrenome).lower()
    data['telefone'] = telefone
    data['email'] = email

    parar = input('Digite (c) para continuar e (p) para encerrar ')
    if parar == "p":
        break
    else:
        continue

def _recebe_dados_json(dados_do_cliente):
    nome_do_cliente = nome + sobrenome
    with open(f'{nome_do_cliente}.json', 'w') as file:
        json.dump(data, file, indent=4)

_recebe_dados_json(dados_do_cliente=data)