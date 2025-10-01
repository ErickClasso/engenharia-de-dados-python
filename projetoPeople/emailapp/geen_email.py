
# Tre, False
# Verdadeiro, Falso
# 1, 0
# sim, nao

# Validador de email
email_padrao = "nome do usuario" + "@" + "nome do dominio" + "." + "extensao"

def geradorEmailCorporativo(nome, sobrenome,empresa, departamento, extensao, sufixo=None):
    dominio = empresa + "_" + departamento
    nome_completo = nome + "." + sobrenome
    email = nome_completo + "@" + dominio + "." + extensao +f"{'' if sufixo is None else '.' + sufixo}"
    return email

#. === condicao intermediario elif
def validadorEmail(email):
    valido = False
    while valido == False:
        if "@" not in email:
            print("Email invalido - sem @")
        elif ' ' in email:
            print("Email invalido - tem espaco")    
        elif '.' not in email:
            print("Email invalido - nao tem ponto")
        elif email.endswith("br"):
            print("Email brasileiro")
        else:
            print("Email estrangeiro")
        valido = True
    return valido

if __name__ == "__main__":

    fabio_classo = geradorEmailCorporativo("fabio","classo", "nttdata", "ti", "com", "br")
    print(f"Email corporativo: {fabio_classo}")
    if validadorEmail(fabio_classo):
        print("Email gerado e validado com sucesso")


    # Melhorias/Proxima aula
    """"
    Funcao de geracao por executar a de validacao
    Usar valores dinamicos (input)
    Ler dados externos (csv, json, xml)
    """