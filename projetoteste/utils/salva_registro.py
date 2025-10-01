#!script/env/bin/python3

import csv 


def salva_registro(cadastro_de_pessoas):
    for pessoa in cadastro_de_pessoas:
        with open('cadastro_de_pessoas.csv', 'a', newline='') as csvfile: # a = append, newline='' para evitar linhas em branco
            writer = csv.writer(csvfile) # vem da biblioteca csv
            writer.writerow(pessoa) # wirteerow escreve uma linha no cadastro_de_pessoas.csv