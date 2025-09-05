
rodada_brasileirao = []
#tuplas
jogo1 = ("Flamengo", "Palmeiras", 2, 1)
jogo2 = ("Vasco", "Botafogo", 0, 0)
jogo3 = ('Fluminense', "Santos", 1, 3)
jogo4 = ("Corinthians", "São Paulo", 1, 2)

#append na lista rodada_brasileirao
# rodada_brasileirao.appemd(jogo1)

for jogo in (jogo1, jogo2, jogo3, jogo4):
    rodada_brasileirao.append(jogo)

# ler os valores da lista rodada_brasileirao
print(f'Rodada do Campeonato Brasileiro: {rodada_brasileirao}')
print()

for jogo in rodada_brasileirao:
    #print(type(jogo))
    #print(f"Rodada do Campeonato Brasileiro: {rodada_basileirao}")

    for resultado in jogo:
        print(resultado, end=", ")
    print()
print()
#dicionarios
jogo_1_dict = {}
#jogo1 = { "Flamengo": 2, "Palmeiras": 1}
jogo_1_dict["Flamengo"] = 2
jogo_1_dict["Palmeiras"] = 1 
print(jogo_1_dict)

#usando for ...
jogo_1_dict_1 = {}
print(jogo1)
time1 = jogo1[0]
time2 = jogo1[1]
gols_time_1 = jogo1[2]
gols_time_2 = jogo1[3]
print(time1, time2, gols_time_1, gols_time_2)

jogo_1_dict_1[time1] = gols_time_1
jogo_1_dict_1[time2] = gols_time_2
print(jogo_1_dict_1)
print()

print("============================")
jogo_1_dict_2 = {}
for x in jogo1:
    time1 = jogo1[0]
    time2 = jogo1[1]
    gols_time_1 = jogo1[2]
    gols_time_2 = jogo1[3]
    jogo_1_dict_2[time1] = gols_time_1
    jogo_1_dict_2[time2] = gols_time_2
print(jogo_1_dict_2)
# fazer o mesmo com os demais times

print()

jogo_2_dict_2 = {}
for x in jogo2:
    time3 = jogo2[0]
    time4 = jogo2[1]
    gols_time_3 = jogo2[2]
    gols_time_4 = jogo2[3]
    jogo_2_dict_2[time3] = gols_time_3
    jogo_2_dict_2[time4] = gols_time_4
print(jogo_2_dict_2)

print()

jogo_3_dict_2 = {}
for g in jogo3:
    time5 = jogo3[0]
    time6 = jogo3[1]
    gols_time_5 = jogo3[2]
    gols_time_6 = jogo3[3]
    jogo_3_dict_2[time5] = gols_time_5
    jogo_3_dict_2[time6] = gols_time_6
print(jogo_3_dict_2)

print()

jogo_4_dict_2 = {}
for y in jogo4:
    time7 = jogo4[0]
    time8 = jogo4[1]
    gols_time_7 = jogo4[2]
    gols_time_8 = jogo4[3]
    jogo_4_dict_2[time7] = gols_time_7
    jogo_4_dict_2[time8] = gols_time_8
print(jogo_4_dict_2)
# =======================================================================================
#=set {}. -vazio não aceita repetição
print()
print("ESTRUTURAS DE DADOS - SET")
times_de_futebol_set = set() # Um conjunto d dados entre chaves {},separads por vigulas
times_de_futebol_set.add("Fluminense") # adicioa Fluminense ao set
times_de_futebol_set.add("Flamengo") # Adiciona flamengo ao set
times_de_futebol_set.add("Vasco") # Adiciona Vasco ao set
print(f"Times de futebol: {times_de_futebol_set}")
print()
print('======================')
times_de_futebol_set.add("Vasco")
times_de_futebol_set.add("Vasco")
times_de_futebol_set.add("Vasco")
times_de_futebol_set.add("Vasco")
times_de_futebol_set.add("Vasco")
print(f"Times de futebol: {times_de_futebol_set}")