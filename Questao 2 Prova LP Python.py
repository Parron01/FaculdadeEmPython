'''
NOME : ANDRE PARRON ARANDA
QUESTAO 2
PROVA B
'''

import math
import numpy as np
#############################################################
#Variáveis
listaDigitosCartao=[]
soma=0
multiplicador=2
#Funçao Principal

for i in range (15):
    x = int(input(f'Insira dígito {i+1}: '))
    listaDigitosCartao.append(x)
    if((x*multiplicador) >9):
        soma = soma + ((x*multiplicador)-9)
    else:
        soma =soma + (x*multiplicador)
    if multiplicador == 2:
        multiplicador=1
    elif multiplicador == 1:
        multiplicador=2
DV=int(input('Digite o dígito verificador: '))
#Descobrindo o DV
if soma%10 == 0:
    DVconferir = 0
else:
    DVconferir = 10 - (soma%10)
#Conferindo se os DVs sao iguais e descobrindo se é válido
if DV == DVconferir:
    print(f'O cartão de crédito inserido é Válido.')
    listaDigitosCartao.append(DVconferir)
    for i in range (16):
        print(listaDigitosCartao[i],end='')
elif (DV != DVconferir):
    print(f'O cartão inserido é Inválido.')
    print('O correto seria = ',end='')
    listaDigitosCartao.append(DVconferir)
    for i in range (16):
        print(listaDigitosCartao[i],end='')

