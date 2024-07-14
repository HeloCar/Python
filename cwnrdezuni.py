numero = int(input('Insira um número menor que 1000 (0 a 999): '))

if numero < 1000:
    centena = numero//100
    if centena > 1:
        print(f'{numero} = {centena} centenas,')
    else:
        print(f'{numero} = {centena} centena,')
    dezena = int((((numero/100)-centena)*100)//10)
    if dezena > 1:
        print(f'{dezena} dezenas e')
    else:
        print(f'{dezena} dezena e')
    unidade = int((((((numero/100)-centena)*100)/10)-dezena)*10)
    if unidade > 1:
        print(f'{unidade} unidades.')
    else:
        print(f'{unidade} unidade.')
