from emailapp.geen_email import geradorEmailCorporativo, validadorEmail
from cadpessoas.registro_de_dados import gravaRegistros

juliana_classo = geradorEmailCorporativo("juliana","classo", "ufsc", "enfermagem", "com", "br")
print(f"Email corporativo: {juliana_classo}")


# validando email

if validadorEmail(juliana_classo):
    print("Email gerado e validado com sucesso")


print()
# gravando registros
cadastro_de_pessoas = set()

# registros de pessoas
fabio = {"nome": "Fabio", "idade": 50, "cidade": "Florianópolis"}
juliana = {"nome": "Juliana", "idade": 48, "cidade": "Florianópolis"}
erick = {"nome": "Erick", "idade": 17, "cidade": "Florianópolis"}
giovanna = {"nome": "Giovanna", "idade": 13, "cidade": "Florianópolis"}
diva = {"nome": "Diva", "idade": 81, "cidade": "Florianópolis"}
ramiro = {"nome": "Ramiro", "idade": 85, "cidade": "Rio de Janeiro"}
taissa = {"nome": "Taissaa", "idade": 48, "cidade": "Rio de Janeiro"}

# forma manual de adicionar pessoas ao cadastro
cadastro_de_pessoas.add(tuple(fabio.items()))
print(f"Cadastro de pessoas: {cadastro_de_pessoas}")
print()

# # criar uma funcao com loop for para adicionar pessoas ao cadastro
for pessoa in [juliana, erick, giovanna, diva, ramiro, taissa]:
    cadastro_de_pessoas.add(tuple(pessoa.items()))
# print(f"Cadastro de pessoas: {cadastro_de_pessoas}")
print()
print(gravaRegistros(cadastro_de_pessoas))