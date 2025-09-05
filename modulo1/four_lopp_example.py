times = ['Fluminense', 'Flamengo', 'Vasco', 'Botafogo']

print(f"tTimes d futebol: {times}")

flamengo = times[1]
print(f"Time selecionado: {flamengo}")

botafogo = times[3]
print(f"Time selecionado: {botafogo}")
print()

#four loop
print("Exemplo de loop:")
for time in ['Fluminense', 'Flamengo', 'Vasco', 'Botafogo']:
    print(time)

print()
for time in times:
    print(time)

# enumerate =========================================================
# 1 - Fluminense
# 2 - Flamengo 
# 3 - Vasco
# 4 - Botafogo
print("Exemplo de for loop com enumerate:") #indices começa em 0 
for numero, time in enumerate(times):
    print(F'{numero} - {time}')

# indice = 1
print()
for numero, time in enumerate(times, start=1):
    print(F'{numero} - {time}')