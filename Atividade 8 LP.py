import math
import numpy as np
#Variaveis

listaAltura =[0]*4
listaNota = [0]*4
data = 0
listaSexo = [0]*4
anoNascimento={}
maiorAltura=0
menorAltura=0
mediaAlturaMulheres=0
mediaNotasMulheres=0
porcentagem=0
soma=0
x=0 
y=0
quantMulheres=0
#Comandos

for i in range (4):
    listaAltura[i] = float(input(f'Digite a sua altura: '))
    listaNota[i] = float(input('Digite a sua Nota: '))
    listaSexo[i] = input('Digite o codigo do seu sexo: \n[M]= Masculino [F]= Feminino\n')
    data = int(input('Digite o seu ano de nascimento: '))
    if data in anoNascimento:
        anoNascimento[data] +=1
    else:
        anoNascimento[data] = 1

#Descobrindo maiores e menores notas
maiorAltura = np.max(listaAltura)
menorAltura= np.min(listaAltura)
#calculando medias
for i in range(4):
    if (listaSexo[i] == 'F' or listaSexo[i] == 'f'):
        quantMulheres+=1
        soma += listaAltura[i]
mediaAlturaMulheres = soma/quantMulheres
quantMulheres=0
soma=0
for i in range(4):
    if (listaSexo[i] == 'F' or listaSexo[i] == 'f'):
        quantMulheres+=1
        soma += listaNota[i]
mediaNotasMulheres = soma/quantMulheres

#printando valores finais

for i in range(4):
    if (listaSexo[i] == 'F' or listaSexo[i] == 'f'):
        if(listaAltura[i] > mediaAlturaMulheres):
            x+=1

for i in range(4):
    if (listaSexo[i] == 'M' or listaSexo[i] == 'm'):
        if(listaNota[i] < mediaNotasMulheres):
            y+=1

print(f'A maior altura da turma é = {maiorAltura} e a menor é = {menorAltura}')
print(f'A quantidade de mulheres acima da média de altura das mulheres é = {x}')
print(f'A quantidade de homens com notas inferiores a média das mulheres é = {y}')

for i in anoNascimento:
    porcentagem = anoNascimento[i]*5
    print(f'A porcentagem de pessoas nascidas em {i} e igual a = {porcentagem}%')