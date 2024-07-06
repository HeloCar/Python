import os

valor_a = int(input('Insira o valor: '))
if valor_a == 0:
    print('Não é uma função do segundo grau')
    exit()
valor_b = int(input('Insira o valor: '))
valor_c = int(input('Insira o valor: '))
delta = (valor_b**2) - 4 * valor_a * valor_c 

if delta < 0:
    print('Não há raízes reais')
    exit()
if delta == 0:
    print('Possui apenas uma raíz real')
if delta > 0:
    print('Possui duas raízes reais')
