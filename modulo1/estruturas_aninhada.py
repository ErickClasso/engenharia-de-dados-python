
cadastro_de_pessoas = set()

#registros de pessoas
fabio = {"nome": "Fabio", "idade": 50, "cidade": "Florianópolis"}
juliana = {"nome": "Juliana", "idade": 48, "cidade": "Florianópolis"}
erick = {"nome": "Érick", "idade": 17, "cidade": "Florianópolis"}
giovanna = {"nome": "Giovanna", "idade": 13, "cidade": "Florianópolis"}
diva = {"nome": "Diva", "idade": 81, "cidade": "Florianópolis"}
ramiro = {"nome": "Ramiro", "idade": 85, "cidade": "Rio de Janeiro"}
taissa = {"nome": "Taíssa", "idade": 28, "cidade": "Rio de Janeiro"}

# forma manual de adicionar pessoas ao cadastro
cadastro_de_pessoas.add(tuple(fabio.items()))
print(f"Cadastro de pessoas: {cadastro_de_pessoas}")

print()

# criar uma função co, loop for para adicionar pessoas ao cadastro
for pessoa in [juliana, erick, giovanna, diva, ramiro, taissa]:
    cadastro_de_pessoas.add(tuple(pessoa.items()))
print(f"Cadastro de pessoas: {cadastro_de_pessoas}")
print()

#exibir cadastro de pessoas:
for i in cadastro_de_pessoas:
    print(i)
print()
# salvar em csv # SÃO AS BIBLIOTECAS PADRAO DO PYTHON

import csv 

for pessoa in cadastro_de_pessoas:
    with open('cadastro_de_pessoas.csv', 'a', newline='') as csvfile: # a = append, newline='' para evitar linhas em branco
        writer = csv.writer(csvfile) # vem da biblioteca csv
        writer.writerow(pessoa) # wirteerow escreve uma linha no cadastro_de_pessoas.csv
#as = aliases (apelidos)