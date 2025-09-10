'''
print(1,2,3,4)
print(2+2)
print('a'+'b')
print('2'+'2')

print('Klewerton')

a = 2
print(a)
print(a+a)
a = 'Ana Paula'
print(a)

a = 3
print(a)

b = 3.2345
print(b)

c = 'Qualquer coisa'
print(c)

d = True
print(d)

a = 123
print('Testando',a)

nome = 'Ana'
print('Olá'+nome)

eggs = 15
bacon = 10
print('nós temos', eggs, 'ovos e', bacon, 'kg de bacon')

ano = 1985 #int
nome = 'Daniel Abella' #str
salario = 10000.50 #float
possuiEmprego = True #bool  

print(type(ano))

n = int(input('digite um número '))
p = int(input('digite outro número '))

media = (n+p)/2

print(f'{media:.2f}')


soma = 0
for i in range(3):
    n = int(input(f'nota {i+1} '))
    soma += n

print(soma)
print(f'Média = {soma/3:.2f}')


n = int(input('Digite o primeiro valor '))
v = int(input('Digite o primeiro valor '))

'''
#operacao = int(input('''Escola a operação:
 #                1 para adição:
  #               2 para subtração:
   #              '''))

#if operacao == 1:
#    print(n+v)
#else:
#    print(n-v)
'''
for i in range(8):
    print(1)
'''

#5. Escreva um programa que use um laço para calcular a soma dos números pares de 1 até n
'''
n = int(input('digite um valor: ')) 
cont = 1
soma = 0 
while cont != n+1:
    if cont % 2 == 0:
        soma += cont
    cont += 1   
print(soma)
#Desafio 57

sexo = input('digite o sexo: ').lower()[0]
while sexo not in 'mf':
    print('Erro')
    sexo = input('digite o sexo: ').lower()[0]

#Desafio 58

from random import randint

n = randint(0,10)
print(n)

v = int(input('tente acertar'))
cont = 1
while v != n:
    print('errou')
    if v < n:
        print('mais')
    elif v > n:
        print('menos')
    v = int(input('tente acertar'))
    cont += 1

print('acertou')
print(cont)

#Desafio 59

v1 = int(input('v1: '))
v2 = int(input('v2: '))
'''
#print('''
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
      #''')
'''
opcao = 0
while opcao != 5:
    opcao = int(input('opção: '))
    if opcao == 1:
        print(f'{v1+v2}')
    elif opcao == 2:
        print(f'{v1*v2}')
    elif opcao == 3:
        print(f'{max(v1,v2)}')
    elif opcao == 4:
        v1 = int(input('v1: '))
        v2 = int(input('v2: '))

#Desafio 60

#Estratégia 1

n = int(input())

res = 1
while n != 0:
    res *= n 
    n -= 1

print(res)
    
#Estratégia 2

n = int(input())
f = n
for i in range(n-1, 0, -1):
    f = f * i 

print(f)

#Desafio 61

term1 = int(input('Informe o primeiro termo de uma PA: '))
razao = int(input('Informe a razão da PA: '))
print()
print('-='*40)
print()

print(f'{term1}', end=' -> ')
cont = 1
soma = term1
while cont <= 9:
    soma += razao
    print(soma, end=' -> ')
    cont+=1
print('Fim')

#Desafio 62

#Estratégia 1

term1 = int(input('Informe o primeiro termo de uma PA: '))
razao = int(input('Informe a razão da PA: '))
print()
print('-='*40)
print()

print(f'{term1}', end=' -> ')
cont = 1
soma = term1
limitador = 9  
while limitador != 0: 
    while cont <= limitador:
        soma += razao
        print(soma, end=' -> ')
        cont+=1
    print('Pausa')
    controlador = int(input('Você quer ver mais quantos números? (para encerrar digite "0") ')) ##
    if controlador == 0:
        limitador = 0
    else:
        limitador += controlador 
     
print('Fim')
print(limitador+1)  ### Bugou aqui !!!

#Estratégia 2

term1 = int(input('Informe o primeiro termo de uma PA: '))
razao = int(input('Informe a razão da PA: '))
print()
print('-='*40)
print()

print(f'{term1}', end=' -> ')
cont = 1
soma = term1 
limitador = 9
controlador = 1
while controlador != 0:
    while cont <= limitador:
        soma += razao
        print(soma, end=' -> ')
        cont+=1
    print('Pausa')
    controlador = int(input('Você quer ver mais quantos números? (para encerrar digite "0") ')) ##
    if controlador != 0:
        limitador += controlador 
     
print('Fim')
print(f'{limitador+1}')

#Desafio 63

n = int(input('digite um número: '))
A = 0
B = 1
print(A,end=' -> ')
print(B,end=' -> ')         
cont = 1
while cont <= n-2:
    if cont != n-2:
        atual = A + B
        print(atual,end=' -> ') 
        A = B
        B = atual
    else:    
        atual = A + B
        print(atual,end=' -> Fim.') 
           
    cont +=1

#Desafio 64

soma = 0
qnum = 0
n = 0
while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n != 999:
        soma += n
        qnum += 1

print(soma)
print(qnum)

#Desafio 65

val = 's'  
soma = 0 
qnum = 0 

while val in 's': 
    n = int(input('Digite um número: ')) 
    soma +=n 
    qnum +=1 
    if qnum == 1: 
        maior = n 
        menor = n 
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    val = (input('Deseja continuar? [S/N] ')).lower()[0] 
    while val not in 'ns': 
        print('Erro, digite uma opção válida') 
        val = (input('Deseja continuar? [S/N] ')).lower()[0] 

print(f'Quantidade de números digitado {qnum}') 
media = soma/qnum 
print(f'média foi: {media}') 

print(maior)
print(menor)

#Desafio 66

cont = soma = 0
while True:

    n = int(input('Digite um valor: [999 para parar] '))
    if n == 999:
        break
    soma += n
    cont += 1

print(soma)
print(cont)

#Desafio 67

while True:
    n = int(input('Quer ver a tabuada de qual valor? (num. negativo para parar) '))
    if n < 0:
        break
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    
#Desafio 68

from random import randint 
from time import sleep
soma = 0

while True:
    while True: 
        opcao = input('Você escolhe par ou impar? ').strip().lower()[0]
        if opcao in 'pi':
            break
        print('Erro! Escolha uma opção válida')

    n = int(input('Digite um número: ')) 
    comp = randint(0,10) 
    print(f'O computador escolheu o número {comp}') 

    if (n+comp) % 2 == 0:
        res = 'par'
    else:
        res = 'impar'

    print(f'Ou seja, deu {res}')
    sleep(1)

    if res[0] != opcao:
        print('Você perdeu!!!')
        break
    soma +=1
    print(f'Até agora você ganhou {soma}')

if soma == 0:
    print('Voce não ganhou nenhuma partida')
else:
    print(f'Foram {soma} vitórias consecutivas')

#Desafio 69

a = b = c = 0
while True:   
    i = int(input('Informe a idade: ')) 
    while True: 
        s = input('informe o sexo [M/F]: ').strip().lower()[0] 
        if s in 'mf': 
            break 
        print('Erro!!! Informe um sexo válido') 
    if i > 18: 
        a += 1 
    if s == 'm': 
        b += 1 
    if s == 'f' and i < 20: 
        c += 1 
    while True: 
        cont = input('Deseja cadastrar mais gente? [S/N]: ').strip().lower()[0] 
        if cont in 'sn': 
            break 
        print('Erro!!! Informe uma opção válida') 
    if cont == 'n': 
        break 

print(f'A) Quantas pessoas com mais de 18 anos? R = {a}')
print(f'B) Quantas homens foram cadastrados? R = {b}')
print(f'C) Quantas mulheres tem menos de 20 anos? R = {c}')
    
#Desafio 70

soma = qtd = cont = 0  

while True: 
    cont += 1 
    n = input('Informe o nome do produto: ') 
    p = float(input('Informe o preço do produto: ')) 
    soma += p 
    if p > 1000: 
        qtd += 1 
    if cont == 1 or p < menor: 
        menor = p 
        produto = n 
    while True: 
        opcao = input('Deseja cadastrar mais produtos? ').strip().lower()[0] 
        if opcao in 'sn': 
            break 
        print('Erro!!! Opção inválida') 
    if opcao in 'n': 
        break 

print(f'A) Total gasto na compra: R$ {soma:.2f}')

if qtd == 0:
    print(f'B) Nenhum produto custou mais de R$ 1.000 reais')
elif qtd == 1:
    print(f'B) {qtd} produto custa mais de R$ 1.000 reais')
else:
    print(f'B) {qtd} produtos custam mais de R$ 1.000 reais')

print(f'C) O produto mais barato foi {produto} e custou R$ {menor:.2f}')

'''
'''
#Desafio 71

#Estratégia 1

print('-='* 30) #######
print(f'{'Bem vindo ao Banco Zabo':^60}') #######
print('-='* 30) #######
print() #######

retirada = int(input('Qual valor a ser sacado? ')) #######

temp = retirada

if temp >= 50:
    print(f'{temp // 50} nota(s) de R$ 50.00')
    temp = temp%50
if temp >= 20:
    print(f'{temp // 20} nota(s) de R$ 20.00')
    temp = temp%20
if temp >= 10:
    print(f'{temp // 10} nota(s) de R$ 10.00')
    temp = temp%10
if temp >= 1:
    print(f'{temp // 1} nota(s) de R$ 1.00')
    temp = temp%1
'''


'''
#Estratégia 2

print('-='* 30)
print(f'{'Bem vindo ao Banco Zabo':^60}')
print('-='* 30)
print()

retirada = int(input('Qual valor a ser sacado? '))

temp = retirada

while True:

    if temp >= 50:
        print(f'{temp // 50} nota(s) de R$ 50.00')
        temp = temp%50
    if temp >= 20:
        print(f'{temp // 20} nota(s) de R$ 20.00')
        temp = temp%20
    if temp >= 10:
        print(f'{temp // 10} nota(s) de R$ 10.00')
        temp = temp%10
    if temp >= 1:
        print(f'{temp // 1} nota(s) de R$ 1.00')
        temp = temp%1

    if temp == 0:
        break


n = int(input('digite o primeiro número: '))
b = int(input('digite o outro número: '))

if n > b:
    print(n)
else:
    print(b)

n = int(input('digite o primeiro número: ')) 
b = int(input('digite o outro número: ')) 

#c = n
#n = b 
#b = c 
n, b = b, n 

print(n, b)


n = int(input('Qual valor do quadrilátero: '))

a = n*n
print(a)

cores = ('amarelo', 'verde', 'cinza', 'roxo', 'aZUl')

for i in cores:
    res = False
    if i.lower() == 'azul':
        res = True

if res:
    print('tem azul')
else:
    print('NÃO tem azul')




#Função
def imc(a, p):
    return p / a**2

#Programa Principal
res = imc(1.85, 95)
print(res)
 
'''

