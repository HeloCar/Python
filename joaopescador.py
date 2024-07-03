peso = float(input('Insira o peso do peixe: '))
excesso = peso - 50
multa = excesso*4

if peso <= 50:
    print('Não pagará multa')
else:
    print('Você deverá pagar multa no valor de: ', multa)