numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))

if numero1 > numero2:
    if numero1 > numero3:
        print('O primeiro número é maior')
    elif numero1 < numero3:
        print('O terceiro número é maior')
elif numero2 > numero1:
    if numero2 > numero3:
        print('O segundo número é maior')
    elif numero2 < numero3:
        print('O terceiro é maior')
