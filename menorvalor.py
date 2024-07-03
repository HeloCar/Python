prod1 = float(input('Informe o valor do primeiro produto: '))
prod2 = float(input('Informe o valor do segundo produto: '))
prod3 = float(input('Informe o valor do terceiro produto: '))

if prod1 < prod2:
    if prod1 < prod3:
        print('Compre o primeiro produto')
if prod1 > prod2:
    if prod2 < prod3:
        print('Compre o segundo produto')
if prod1 > prod3:
    if prod3 < prod2:
       print('Compre o terceiro produto')