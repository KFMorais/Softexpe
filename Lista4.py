'''
#Questão 1
# 1. Faça um Programa que leia 5 números inteiros, armazene-os em uma lista.

lista = []
for i in range(5):
    lista.append(int(input(f'Digite o {i+1}º número: ')))

print(lista)

#Questão 2
# 2. Faça um Programa que leia 10 números reais e mostre-os na ordem inversa.

lista = []
for i in range(10):
    lista.append(float(input(f'Digite o {i+1}º número: ')))

for j in range((len(lista)-1), -1, -1):
    print(lista[j], end=' ')
print()

print(lista)

#Questão 3
# 3. Faça um Programa que leia 40 notas, mostre as notas e a média na tela.

soma = 0
notas = []
for i in range(40):
    n = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(n)
    soma += n

media = soma/40

print(f'As notas informadas foram {notas} e a média delas é {media}')

#Questão 4
# 4. Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os
#números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas.

total = []
lp = []
li = []

for i in range(20):
    n = int(input(f'Digite o {i+1}º número: '))
    total.append(n)
    if n % 2 == 0:
        lp.append(n)
    else: 
        li.append(n)

print(total)
print(lp)
print(li)

#Questão 5
# 5. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa
#lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []
ana = 0

for i in range(10):
    soma = 0
    for j in range(4):
        n = float(input(f'Digite a {j+1}ª nota do {i+1}º aluno: '))
        soma += n
    media = soma/4
    medias.append(media)
    if media >= 7:
        ana +=1

print(f'A media dos alunos foram: {medias}')
print(f'{ana} alunos tiveram media igual ou superior a 7,0')

#Questão 6
#6. Faça um Programa que leia e armazene 50 números inteiros, mostre a soma, a
#multiplicação e os números.

numeros = []
soma = 0
mult = 1
for i in range(50):
    n = int(input(f'Digite o {i+1}º numero: '))
    numeros.append(n)
    soma += n
    mult *= n  

print(numeros)
print(soma)
print(mult)

#Questão 7
#7. Faça um Programa que peça a idade e a altura de 10 pessoas, armazene cada
#informação na sua respectiva lista. Imprima a idade da pessoa que possui maior altura.

idade = []
altura = []
maior_altura = 0

for z in range(10):
    i = int(input(f'informe a idade da {z+1}ª pessoa: '))
    idade.append(i)
    a = float(input(f'informe a altura da {z+1}ª pessoa: '))
    altura.append(a)
    if a > maior_altura:
        maior_altura = a
        idade_m_al = i

print(idade_m_al)

#Questão 8
#8. Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a
#soma dos quadrados dos elementos do vetor.

A = []
soma = 0
for i in range(10):
    n = int(input(f'Digite o {i+1}º número: '))
    A.append(n)
    q = n**2
    soma += q

print(soma)

#Questão 9
#9. Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos,
#cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas.

#Estratégia1

l1 = []
l2 = []
l3 = []

for i in range(1,11):
    v1 = int(input(f'Digite o {i}º valor da 1ª lista: '))
    v2 = int(input(f'Digite o {i}º valor da 2ª lista: '))
    l1.append(v1)
    l2.append(v2)
    l3.append(v1)
    l3.append(v2)


print(l1)
print(l2)
print(l3)

#Estratégia2
l1 = []
l2 = []
l3 = []

for i in range(1,11):
    v1 = int(input(f'Digite o {i}º valor da 1ª lista: '))
    l1.append(v1)
    l3.append(v1)

pos = 1
for j in range(1,11):
    v2 = int(input(f'Digite o {j}º valor da 2ª lista: '))
    l2.append(v2)
    l3.insert(pos, v2)
    pos += 2
    

print(l1)
print(l3)
print(l2)
'''

#Questão 10
# 10. Altere o programa anterior, intercalando

#Não há informações suficientes para responder essa questão... Creio que há erro no enunciado 
# (ausencia de informações)
