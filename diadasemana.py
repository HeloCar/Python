numero = int(input('Digite um número correspondente ao dia da semana (1 a 7): '))
semana = {1 : ['Domingo'],
          2 : ['Segunda'],
          3 : ['Terça'],
          4 : ['Quarta'],
          5 : ['Quinta'],
          6 : ['Sexta'],
          7 : ['Sábado']}

if numero in semana:
    print(semana[numero])
else:
    print('Valor inválido')
       