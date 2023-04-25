import math
#VARIAVEIS
digitocontrole = [0]*2
soma = 0
a=0
x=10
resto=0
#RECEBENDO O CPF
listaCpf = list(map(int, input(f'digite todos os numeros [exceto os 2 ultimos] do CPF separados por espaço: ').split(" ")))
print(listaCpf)
for i in range(9):  
    soma = soma + (listaCpf[i]*x)
    x-=1

cpfcontrole = list(map(int, input(f'Digite os 2 ultimos dígitos de controle separados por espaço: ').split(" ")))
print('')    

#FAZENDO O PRIMEIRO PASSO PARA DESCOBRIR PRIMEIRO DIGITO DE CONTROLE
resto = soma%11
if resto == 0 or resto == 1:
    digitocontrole[0]=0
elif resto >=2:
    digitocontrole[0] = 11 - resto
    listaCpf.append(digitocontrole[0])


#SEGUNDO PASSO PARA DESCOBRIR O SEGUNDO DIGITO DE CONTROLE
x=11
soma=0
resto=0
for i in range(10):
    soma += listaCpf[i]*x
    x-=1
resto = soma%11
if resto == 0 or resto == 1:
    digitocontrole[1]=0
elif resto >=2:
    digitocontrole[1] = 11 - resto
    listaCpf.append(digitocontrole[1])

#CONFERINDO SE CPF E VALIDO OU NAO E PRINTANDO A RESPOSTA
if cpfcontrole[0] == listaCpf[9] and cpfcontrole[1] == listaCpf[10]:
    print(f'CPF VÁLIDO: ')
    for i in range(11):
        print(listaCpf[i], end="")
        a+=1
        if a==3 or a==6:
            print('.',end="")
        elif a == 9:
            print('-',end="")
    print('')
else:
    print(f'CPF INVÁLIDO.')
    print(f'Os digitos de controle corretos seriam = {listaCpf[9]} e {listaCpf[10]} em vez de {cpfcontrole[0]} e {cpfcontrole[1]}\n')
