
# True, False
# VErdadeiro, Falso
# 1, 0
# sim, não

email_padrao = "nome do usuario" + "@" + "." + "extensao"
""""
Validação:
se não tem "@" = email invalido
"""
# string - endswith
# se o email termina com "br" - email brasileiro.

# valido = False
# while valido == False:
#     emaail_usuario2 = "frclasso@yahoo.com.br"
#     if "@" not in emaail_usuario2:
#         print("Email invalido - sem @")
#         break
#     else:
#         if ' ' in emaail_usuario2:
#             print("Email invalido - tem espaço")
#             break
#         else:
#             if '.' not in emaail_usuario2:
#                 print("Email invalido - não tem ponto")
#                 break
#             else:
#                 print("Email valido.")
#                 if emaail_usuario2.endswith("br"):
#                     print("Email brasileiro")
#                 else:
#                     print("Email estrangeiro")
#                 valido= True

#. === condição intermediario elif

def validadorEmail(email):
    valido = False
    while valido == False:
        if "@" not in email:
            print("Email invalido - sem @")
        elif ' ' in email:
            print("Email invalido - tem espaço")
        elif '.' not in email:
            print("Email invalido - não tem ponto")
        elif email.endswith("br"):
            print("Email brasileiro")
        else:
            print("Email estrangeiro")
        valido = True
    return valido

email_erick = "erick_#email.com"
email_erick = "erick_@email.com"
email_erick = "erick_@email.com.br"
validadorEmail(email_erick)