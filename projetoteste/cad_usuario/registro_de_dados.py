from utils.salva_registro import salva_registro

# Exibir cadastro de pessoas
def gravaRegistros(cadastro_de_pessoas):
    for registro in cadastro_de_pessoas:
        salva_registro(registro)
    return f"Registros gravados com sucesso"
# salvar em csv
# SAO AS BIBLIOTECAS PADRAO DO PYTHON


# as = aliases (apelidos) 
