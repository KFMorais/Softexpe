entrada = []

for i in range(2):
    entrada.append(int(input(f'digite o {i+1}º valor: ')))

print('''Escolha a operação:
            0- Adição
            1- Subtração
            2- Multiplicação
            3- Divisão 
      ''')

opcao = int(input(': '))
while opcao > 3 or opcao < 0:
    print('Erro!!! Escolha uma opção válida!')
    opcao = int(input(': '))

if opcao == 0:
    print(entrada[0]+entrada[1])
elif opcao == 1:
    print(entrada[0]-entrada[1])
elif opcao == 2:
    print(entrada[0]*entrada[1])
elif opcao == 3:
    print(entrada[0]/entrada[1])
