import pandas

dados_clientes = pandas.read_csv("people_1.csv")
# print(dados_clientes)
print()
# 5 primeiras linhas
print(dados_clientes.head())
print()
# 5 Últimas linhas 
print(dados_clientes.tail())
print()
# output customizado
print(dados_clientes.head(100)) # cem primeiros
print()
# informações do dataframe
familia_azevedo = []
sobrenome = "Azevedo"
for user in dados_clientes.values:
    for client in user:
        if client == sobrenome:
            # print(f"Cliente. {sobrenome} encontrado")
            #print(user)
            print(type(user))
            familia_azevedo.append(user)
            break

print()
for nome in familia_azevedo:
    print(nome)
print()
# dataframe familia azevedo
azevedo_df = dados_clientes.get(dados_clientes['last_name'] == 'Azevedo')
print(azevedo_df)
print()
# salvando dados em csv
azevedo_df.to_csv("familia_azevedo.csv", index=False)

