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
'''

#Questão 4

for i in range(2, 21, 2):
    print(i, end=' -> ')
print('Fim')


