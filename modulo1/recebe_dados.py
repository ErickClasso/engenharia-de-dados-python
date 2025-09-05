import json

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
telefone = input("Telefone: ")
email = input("Email: ")

data = {}
data['nome'] = nome
data['sobrenome'] = sobrenome
data['telefone'] = telefone
data['email'] = email

with open('erick_contacts.json', 'w') as file:
    json.dump(data, file, indent=4)



# leitor
with open('erick_contacts.json', 'r',) as file:
    file_data = json.load(file)
    print(file_data)


# leitor2
with open('erick_contacts.json', 'r',) as file:
    file_data = json.load(file)
    json_data = json.dumps(file_data, indent=4)
    print(json_data)
