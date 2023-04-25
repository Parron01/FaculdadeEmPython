'''
NOME : ANDRE PARRON ARANDA
QUESTAO 1
PROVA B
'''

import math
import numpy as np
#############################################################
#Variáveis
listaGenero = []
listaIdade =[]
listaSalario = []
listaRespostas = []
sim=0
nao=0
porcentagemSim=0
porcentagemNao=0

#############################################################
def Estatistica1(listaSalario1,listaIdade1):
    x=0
    y=0
    x=np.mean(listaSalario1)
    y=np.mean(listaIdade1)
    return(x,y)
#############################################################
def Estatistica2(listaIdade2,listaGenero2,listaRespostas2):
    quant=0
    soma=0
    media=0
    for i in range (n):
        if(listaGenero2[i] == 'M'):
            if(listaRespostas2[i] == 'nao'):
                quant+=1
                soma = soma + listaIdade2[i]
    media = soma/quant
    return media
#############################################################
def Estatistica3(listaSalario3):
    faixaA=0
    faixaB=0
    faixaC=0
    faixaD=0
    for i in range(n):
        if(listaSalario3[i]>10000):
            faixaA+=1
        if(listaSalario3[i]>5000.01 and listaSalario3[i]<=10000):
            faixaB+=1
        if(listaSalario3[i]>2500.01 and listaSalario3[i]<=5000):
            faixaC+=1
        if(listaSalario3[i]<=2500):
            faixaD+=1
    return (faixaA,faixaB,faixaC,faixaD)
#############################################################
#FUNÇAO PRINCIPAL
n=int(input('Quantas pessoas serão entrevistadas?: '))
for i in range(n):
    x=input('Digite o seu gênero: [M] ou [F]\n')
    listaGenero.append(x.upper())
    x=int(input('Digite sua idade: '))
    listaIdade.append(x)
    x=float(input('Digite o seu salário: '))
    listaSalario.append(x)
    x=input('Você compraria o produto? [sim] ou [nao]:\n')
    listaRespostas.append(x.lower())
for i in range (n):
    if(listaRespostas[i] == 'sim'):
        sim+=1
    elif(listaRespostas[i] == 'nao'):
        nao+=1

porcentagemSim =(100/n)*sim
porcentagemNao =(100/n)*nao

print(f'\nPorcentagem de pessoas que não comprariam = {porcentagemNao:.2f}%\nPorcentagem de pessoas que comprariam = {porcentagemSim:.2f}%\n')

listaMediasSalarioIdade = Estatistica1(listaSalario,listaIdade)
print(f'A média dos salarios é de = {listaMediasSalarioIdade[0]:.2f} e a média das idades é de = {listaMediasSalarioIdade[1]:.2f}\n')

mediaIdadeHomensNao = Estatistica2(listaIdade,listaGenero,listaRespostas)
print(f'A media das idades das pessoas do sexo masculino e que responderam nao é de = {mediaIdadeHomensNao:.2f}\n')

listaFaixas = Estatistica3(listaSalario)
print(f'Pessoas na faixa A = {listaFaixas[0]}\nPessoas na faixa B = {listaFaixas[1]}\nPessoas na faixa C = {listaFaixas[2]}\nPessoas na faixa D = {listaFaixas[3]}\n')