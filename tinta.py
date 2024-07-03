a = float(input('Qual o tamanho da área a ser pintada? '))
b = round((a/3)/18)
c = b*80

if b < 1:
    print('O cliente precisará de uma lata e o valor total será R$80,00')
else:
    print(f'O total de latas será {b} e o valor total R${c}')