'''
#Questão 1

soma = 0
while True:
    n = int(input('Digite um número [0 para encerrar]: '))
    if n == 0:
        break
    soma += n

print(f'A soma dos valores informados é: {soma}')

#Questão 2

while True:
    s = input('Digite sua senha: ')
    if s == 'python123':
        break
    print('Senha inválida, Tente novamente...')

print('Login realizado com sucesso')

#Questão 3

v = int(input('Digite um valor para fins de cálculo de tabuada: '))
print()
cont = 0
while True:
    print(f'{v} x {cont} = {v*cont}')
    cont += 1
    if cont == 11:
        break

#Questão 4

for i in range(2, 21, 2):
    print(i, end=' -> ')
print('Fim')

#Questão 5

for i in range(5):
    n = int(input(f'Digite o {i+1} número '))
    if i == 0 or n > maior:
        maior = n

print(maior)

#Questão 6

n = input('Digite uma palavra: ')
soma = 0
for i in n:
    if i in 'aeiou':
        soma += 1
print(soma)

#Questão 7

def adicao(a,b):
    s = a+b
    return s


print(adicao(3,5))

#Questão 8

def népar(t):
    if t % 2 == 0:
        return True
    else:
        return False

print(népar(7))
print(népar(4))
print(népar(0))

#Questão 9
#Estratégia 1

def media(i):
    soma = 0
    for f in i:
        soma += f
    media = soma/len(i)
    return media


numeros = [10, 8, 10, 8]
print(media(numeros))

#Questão 9
#Estratégia 2

def media(*i):
    soma = 0
    for f in i:
        soma += f
    media = soma/len(i)
    return media


print(media(10, 8, 10, 8, 10, 8))
'''

#Questão 10

def saudacao(nome):
    print('-'*(len(nome)+27))    
    return  f'"Olá, {nome}! Seja bem vindo(a)!"' 


print(saudacao('Klewerton'))
print(saudacao('José'))