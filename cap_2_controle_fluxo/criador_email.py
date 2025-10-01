criador_email = []

print("Para criar o email, basta seguir o passo a passo:")

while True:
    nome = input("digite seu nome: ")
    sobrenome = input("digite seu sobrenome: ")
    nome_C = nome.lower() + sobrenome.lower()
    
    print("Escolha seu provedor de email:")
    print("1 - Gmail")
    print("2 - Yahoo")
    print("3 - Hotmail")
    provedor = (input("Digite o número da opção desejada: "))
    if not provedor.isnumeric():
        print("Você precisa digitar um número.")
        continue
    
    if int(provedor) >=4:
        print("Digite um número entre '1 e 3'")
        print("Tente novamente.")
        continue
    provedor = str(provedor)

    email = nome_C + "@"

    if provedor == "1":
        email = email + "gmail.com"
    if provedor == "2":
        email = email + "yahoo.com.br"
    if provedor == "3":
        email = email + "hotmail.com"

    criador_email.append(email)     
    break

print(f"Seu email foi criado: {criador_email}, agora vamos fazer sua senha.")

while True:
    
    senha = input(f"Crie sua senha: ")

    
    if len(senha) < 8:
        print("Senha muito curta!")
        print("Sua senha deve conter no mínimo '8' caracteres. Tente novamente.")
        continue
    if senha == "12345678":
        print("Senha muito simples, reforçe sua senha.")
        continue
    
    senha_secreta = ''
    for n in senha:
        senha_secreta += "*"

    C_Senha = input(f"Por segurança confirme sua senha: ")
    if not C_Senha == senha:
        print(f"A senha que você digitou não bate com esta {senha_secreta}. ")
        C_Senha = input(f"tente novamente: ")
        if not C_Senha == senha:
            print("Ok vamos fazer denovo.")
            continue 
    criador_email.append(senha)
    print("Senha criada com sucesso!")
    break
print(criador_email)
print("Agora vamos logar na sua conta.")

while True:
    logar = input("Digite seu email: ")
    if criador_email[0] == logar:
        print("email encontrado.")
    else:
        print("Email não encontrado.")
        continue

    log_senha = input("Digite sua senha: ")
    if log_senha == criador_email[1]:
        print('Conta logada com sucesso!')
    else:
        print("Senha errada, por favor tente novamente.")
        continue
    break