import csv

with open('cadastro_de_pessoas.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ' ', quotechar= '|')
    for row in spamreader: # row = linha - spamreader = leitor de linha
        print(', '.join(row))

print()
line = ["('nome',, 'Fabio')","('idade',, 50)","('cidade',, 'Florianópolis')"]
print(type(line[0])) # " entre aspas =string
print(line[0])

# Alteração
# valor de cidade: Rio de Janeiro
line[2] = "('cidade', 'Rio de Janeiro')"
print(line)

with open('cadastro_de_pessoas.csv', newline='') as csvfile:
    lines = csv.reader(csvfile, delimiter= ' ')
    for line in lines:
        if line[0] == "('nome', 'Fabio')": # condição se (if) o nome for Fabio, printou o nome
            print(line[0]) # Encontrado
            # alterar o valor de cidade
            line[2] = "('cidade', 'Rio de Janeiro')"
            print(line)

print()
# Mudar os tipos de dados
idade = "35"
nome= "Erick"
print(f"Nome: {nome}, Idade: {idade}")

salario = 2500.50 # float/numerico /decimal
aumento = "500.75" # string
# total_recebido = salario + aumento #erro
total_recebido = salario + float(aumento) #erro
print(total_recebido)


# Funcoes - criar um espaço isolado no codigo, que pode ser reaproveitado
def altera_cidade(nome_da_pessoa):
    with open('cadastro_de_pessoas.csv', newline="") as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for line in lines:
            if line[0] == f"('nome', '{nome_da_pessoa}')":  #condicao se (if) o nome for Fabio , printou o nome
                # print(line[0]) # encontrado
                # print(nome_da_pessoa)
                # Alterar o valor de cidade
                line[2] = "('cidade', 'Rio de Janeiro')"
                print(line)

# chamada da funcao = nome da função + ()
altera_cidade(nome_da_pessoa="Ramiro")
print()
# reaproveitado
altera_cidade(nome_da_pessoa="Taissa")
altera_cidade(nome_da_pessoa="Erick")
altera_cidade(nome_da_pessoa="Giovanna")