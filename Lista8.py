'''
#Questão 1
#Use a biblioteca random para sortear um número entre 1 e 100.

from random import randint

print(randint(1,100))

#Questão 2
#Crie uma lista de nomes e use random.choice() para escolher um vencedor.
import random

lista_nomes = ['Klewerton', 'Eu', 'Eu mesmo']
print(random.choice(lista_nomes))

#Questão 3
#Use a biblioteca datetime para mostrar a data e hora atuais.
from datetime import datetime

agora = datetime.now()
print(agora.strftime('%H:%M:%S'))
print(agora.strftime('%d/%m/%Y'))

#Questão 4
#Com math, calcule a potência de 2 elevado a 10.

from math import pow

print(int(pow(2,10)))
'''

#Questão 5
#Instale a biblioteca requests e faça uma requisição para o site https://www.google.com.

import requests

site = 'https://www.google.com'

resp = requests.get(site)

if resp.status_code == 200:
    print('Deu certo')
    html_pagina = resp.text
    print(html_pagina[:500])
