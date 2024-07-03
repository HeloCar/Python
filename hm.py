a = input('Você é homem ou mulher? ')
b = float(input('Qual a sua altura? '))
c = (72.7*b) - 58
d = (62.1*b) - 44.7

if a == 'mulher':
    print('Seu peso ideal é ', d)
else:
    print('Seu peso ideal é: ', c)