'''
#Questão 1
# Crie uma lista com os números de 1 a 5 e exiba na tela.

a = [1, 2, 3, 4, 5]
print(a)

#Questão 2
#Dada a lista cores = ["azul", "verde", "vermelho", "amarelo"], exiba apenas a segunda e a última cor.

cores = ['azul', 'verde', 'vermelho', 'amarelo']
print(cores[1], cores[len(cores)-1])

#Questão 3
#Crie uma lista com três frutas e substitua a segunda fruta por "abacaxi".

frutas = ['abacate', 'banana', 'maça']
frutas[1] = 'abacaxi'
print(frutas)

#Questão 4
#Peça ao usuário para digitar 5 números e armazene-os em uma lista. Depois exiba a lista completa.

casa = list()
for i in range(5):
    n = int(input('Digite um número: '))
    casa.append(n)
print(casa)

#Questão 5
#Crie uma lista com valores numéricos [8, 3, 10, 1, 7], ordene em ordem crescente e exiba o resultado.

n = [8, 3, 10, 1, 7]
n.sort(reverse=True)
print(n)

#Questão 6
#Peça ao usuário para inserir 5 números em uma lista e calcule a soma total.

numeros = []
soma = 0
for i in range(5):
    n = int(input('Digite um número: '))
    numeros.append(n)
    soma += n

print(soma)
print(numeros)

#Questão 7
# Dada uma lista de inteiros, exiba o maior e o menor valor.

n = [1,5,7,3]
print(max(n))
print(min(n))

#Questão 8
# Dada a lista letras = ["a", "b", "a", "c", "a", "d"], conte quantas vezes a letra "a" aparece.

c = ['a', 'b', 'a', 'c', 'a', 'd']
soma = 0
for i in c:
    if i == 'a':
        soma += 1

print(soma)

#Questão 9
# Dada a lista numeros = [2, 4, 6, 8, 10], remova o número 6 e mostre a lista atualizada.

numeros = [2, 4, 6, 8, 6, 10]

while 6 in numeros:
    numeros.remove(6)

print(numeros)

#Questão 10
#Peça ao usuário um número N e crie uma lista com todos os números pares de 1 até N.

casa = []
n = int(input('digite um número: '))
for i in range(2, n+1,2):
    casa.append(i)

print(casa)

#Questão 11
# Crie uma tupla com os dias da semana e exiba o terceiro dia.

diasdasemana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
print(diasdasemana[2])

#Questão 12
# Explique o que acontece ao tentar alterar um elemento de uma tupla. Faça o teste no código.

teste = ('agua', 'suco')
teste.append('arroz')

#Questão 13
#Crie uma lista de 5 nomes, converta-a em tupla e exiba os dois tipos.

nomes = ['Klewerton', 'Jose', 'Astrogildo', 'Claudia', 'Bigode']
print(nomes)
tup = tuple(nomes)
print(tup)

#Questão 14
#Dada a tupla t = (5, 10, 15, 20), calcule e exiba a soma dos valores.

t = (5, 10, 15, 20)
print(sum(t))
'''

#Questão 15
#Crie uma tupla com números e verifique se um número digitado pelo usuário está dentro da tupla.

d = (1,5,9,14)
n = int(input('Digite um número: '))

if n in d:
    print(True)
else:
    print(False)
