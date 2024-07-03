tamanho = int(input('Qual o tamanho do arquivo em MB? '))
velocidade = int(input('Qual a velociade do link de internet em Mbps?'))
calculo = tamanho/velocidade/8
tempomin = calculo*60

print(f'O tempo de download será de {tempomin} minutos.')