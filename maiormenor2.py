numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))

if numero1 > numero2:
    if numero1 > numero3:
        print('O primeiro número é maior')
        if numero2 < numero3:
            print('O segundo é o menor')
        elif numero2 > numero3:
            print('O terceiro é o menor')
    elif numero1 < numero3:
        print('O terceiro número é maior e o segundo o menor')
elif numero2 > numero1:
    if numero2 > numero3:
        print('O segundo número é maior')
        if numero1 > numero3:
            print('O terceiro é o menor')
        elif numero1 < numero3:
            print('O primeiro é o menor')
    elif numero2 < numero3:
        print('O terceiro é maior e o primeiro o menor')
elif numero1 < numero3:
    if numero2 < numero3:
        print('O terceiro é o maior')
        if numero1 < numero2:
            print('O primeiro é o menor')
        elif numero1 > numero2:
            print('O segundo é o menor')