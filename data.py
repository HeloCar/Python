dia = int(input('Digite uma data válida, insira o dia primeiramente no formato dd: '))
mes = int(input('Digite o mês no formato mm: '))
ano = int(input('Digite o ano no formato aaaa: '))

if dia > 31 or mes > 12 or ano < 0:
    print('Não é uma data válida')
else:
    print('É uma data válida')