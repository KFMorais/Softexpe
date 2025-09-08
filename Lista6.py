'''
List Comprehension em Python6. Atividades para fixação

#1- Crie uma lista com os quadrados dos números de 1 a 20.

lista = [i**2 for i in range(1, 21)]
print(lista)

#2- Crie uma lista apenas com os números pares de 0 a 50.

lista = [x for x in range(51) if x % 2 == 0]
print(lista)

#3- Dada a string "comprehension", crie uma lista com apenas as vogais.

lista = [x for x in 'comprehension' if x in 'aeiou']
print(lista)

#4- Gere uma lista de números múltiplos de 3 entre 0 e 30.

lista = [x for x in range(0,31,3)]
print(lista)

'''
#5- Crie uma lista de tuplas (n, n²) para n de 1 a 10.

lista = [(x, x**2) for x in range(1,11)]
print(lista)