
vh = float(input('Digite o valor recebido por hora trabalhada: [R$] '))
ht = float(input('Informe a quantidade de horas trabalhadas no mês: '))
print()

sb = vh * ht
print(f'{'+ Salário bruto':<21} R$ {sb:.2f}')
ir = sb*11/100
print(f'{'* IR (11%)':<21} R$ {ir:.2f}')
inss = sb*8/100
print(f'{'* INSS (8%)':<21} R$ {inss:.2f}')
sind = sb*5/100
print(f'{'* Sindicado (5%)':<21} R$ {inss:.2f}')
sl = sb - ir - inss - sind
print()
print(f'{'+ Salário líquido':<21} R$ {sl:.2f}')
print()



