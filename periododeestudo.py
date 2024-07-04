turno = input('Informe o período que você estuda (M: Matutino, V: Vespertino, N: Noturno): ')

if turno == 'm' or turno == 'M':
    print('Bom dia! Bons estudos!')
elif turno == 'v' or turno == 'V':
    print('Boa tarde! Bons estudos!')
else:
    print('Boa noite! Bons estudos!')