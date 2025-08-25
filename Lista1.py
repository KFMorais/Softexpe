'''
#Questão 1

lista = []

for i in range(5):
    lista.append(int(input()))

for j in range(5):
    print(lista[j],end=' ')
print()

for k in range(4, -1, -1):
    print(lista[k], end=' ')
print()

#Questão 2

v = int(input('digite o primeiro valor '))
x = int(input('digite o segundo valor '))

print(f'{v-x}')

#Questão 3

notas = []
for i in range(4):
    notas.append(int(input('digite a nota: ')))
soma = 0
for z, j in enumerate(notas):
    print(f'{z+1}º nota: {j}')
    soma += j

media = soma/len(notas)

print(f'A média do aluno foi: {media}')

#Questão 4

n = int(input('digite um número: '))

print(f'{n**0.5}')

#Questão 5

a = int(input('digite a medida de um dos lados: '))

print(f'A área do quadrado é: {(a**2)}')
print(f'O volume do cubo é: {(a**3)}')

#Questão 6

salario = float(input('Quanto você ganha por hora: '))
ht = float(input('Qual número de horas trabalhadas no mês: '))

print(f'Seu salário bruto será de R$ {salario*ht:.2f}')
'''

