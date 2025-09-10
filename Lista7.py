'''
#Questão 1
#Crie uma função que receba um número e retorne o seu quadrado.

def quadrado(x):
    return x**2

res = quadrado(8)
print(res)

#Questão 2
#Crie uma função que receba dois números e retorne o maior deles.

def num_maior(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return f'Os valores informados são iguais'
        
res = num_maior(8, 5)
print(res)

#Questão 3
#Crie uma função que receba uma lista de números e retorne a soma.

def soma_num(*n):
    soma = 0
    for i in n:
        soma += i
    return soma

res = soma_num(2,5,7,9)
print(res)

'''
#Questão 4
#Crie uma função que mostre a tabuada de um número.

def tab(n):
    mult = 1
    for i in range(11):
        print(f'{n} x {i} = {n*i}')

tab(4)
