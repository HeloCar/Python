inicio = float(input('Informe a área em metros quadrados a ser pintada: '))
formadeprod = input('Qual o formato do produto? (lata, galao, misto)')
totallata = round(inicio/6/18)
totalgalao = round(inicio/6/3,6)
totalmisto = round(totallata + totalgalao)
valorlata = float(totallata*80)
valorgalao = float(totalgalao*25)
valormisto = float(valorlata + valorgalao)


if formadeprod == 'lata':
    print(f'Sera(o) necessario(s) {totallata} lata(s) e o valor total será R${valorlata}')
if formadeprod == 'galao':
    print(f'Sera(o) necessario(s) {totalgalao} galão(s) e o valor total será R${valorgalao}')
if formadeprod == 'misto':
    print(f'Sera(o) necessario(s) {totallata} lata(s), {totalgalao} de galão(s), totalizando {totalmisto} de recipientes. O valor total será R${totalmisto}')





