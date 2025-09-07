'''
#Questão 1
# 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.

livros = ['Entendendo Algotírimos','O Senhor do Aneis', 'Cinco minutos']
print(livros)

#Questão 2
# 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.

livros = ['Entendendo Algotírimos','O Senhor do Aneis', 'Cinco minutos']
print(f'1º livro da lista: {livros[0]} e Último livro da lista: {livros[2]}')

#Questão 3
# 3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.

livros = ['Entendendo Algotírimos','O Senhor do Aneis', 'Cinco minutos']
livros.append('Narnia')
livros.append('Hugo')
print(livros)

#Questão 4
# 4- Insira o livro "Duna" na segunda posição da lista livros usando insert().

livros = ['Entendendo Algotírimos','O Senhor do Aneis', 'Cinco minutos']
livros.insert(1, 'Duna')
print(livros)

#Questão 5
# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".

#Situação 1
livros = ['Entendendo Algotírimos', 'O Senhor do Aneis', 'Silêncio dos inocentes', 'Cinco minutos']
livros.remove('Silêncio dos inocentes')
print(livros)

#Situação 2
livros = ['Entendendo Algotírimos', 'O Senhor do Aneis', 'Silêncio dos inocentes', 'Cinco minutos']
print(livros)
if 'Silêncio dos inocentes' in livros:
    livros.remove('Silêncio dos inocentes')
else: 
    print('Livro não encontrado')
print(livros)

#Questão 6
# 6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.

numeros = [1, 2, 3, 2, 4, 2, 5]
print(numeros.count(2))

#Questão 7
# 7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"

livros = ['Entendendo Algotírimos','O Senhor do Aneis', 'Cinco minutos']

for livro in livros:
    print(f'O livro {livro} é interessante')

#Questão 8
# 8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.

idades = [12, 18, 25, 14, 30]

for idade in idades:
    if idade >= 18:
        print(idade)

#Questão 9
# 9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.

valores = [10, 20, 30, 40]

soma = 0
for valor in valores:
    soma += valor

print(soma)

#Questão 10
# 10- Use input para receber 3 notas de dois alunos. 
# As notas de cada aluno precisam ser armazenadas em uma lista separada que
# deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

notas = [[], []]
medias = []

for i in range(2):
    soma = 0
    for j in range(3):
        nota = float(input(f'Informe a {j+1}º nota do {i+1}º aluno: '))
        notas[i].append(nota)
        soma += nota
    media = soma/3
    medias.append(media)

print(f'As notas do primeiro aluno são: {notas[0]} e do segundo aluno são: {notas[1]}')
print(f'A média do primeiro aluno é: {medias[0]} e do segundo aluno é: {medias[1]}')
'''

#Questão 11
# 11- Usando list comprehension, crie um tabuleiro de xadrez vazio e 
# depois adicione todas as peças do jogo na posição inicial. 
# Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
#[ ] - para posições vazias
#tor - para a torre
#cav - para o cavalo
#bis - para o bispo
#rai - para a rainha
#rei - para o rei
#pea - para o peão
#Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. 
# (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)

for i in range(8):
    for j in range(8):
        if i == 0 or i == 7:
            if j == 0 or j == 7:
                print('[tor]', end=' ')
            elif j == 1 or j == 6:
                print('[cav]', end=' ')
            elif j == 2 or j == 5:
                print('[bis]', end=' ')
            elif j == 3:
                print('[REI]', end=' ')
            elif j == 4:
                print('[rai]', end=' ')
        elif i == 1 or i == 6:
            print('[pea]', end=' ')
        else: 
            print('[   ]', end=' ')
    print()
