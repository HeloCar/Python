valorhora = float(input('Valor da hora: R$'))
salariobruto = valorhora*(8*30)


def desconto_ir(salariobruto):
    if salariobruto <= 900:
        salariobruto = 'ISENTO'
    if salariobruto > 900:
        if salariobruto <= 1500:
           desconto = '5%'
           salariobruto = salariobruto*0.05
    if salariobruto > 1500:
        if salariobruto <= 2500:
           desconto = '10%'
           salariobruto = salariobruto*0.1
    if salariobruto > 2500:
        desconto = '20%'
        salariobruto = salariobruto*0.2
    return(f'(-) IR ({desconto})              :R${salariobruto}')

if salariobruto <= 900:
        salariodesc = 'ISENTO'
if salariobruto > 900:
    if salariobruto <= 1500:
        salariodesc = salariobruto*0.05
if salariobruto > 1500:
    if salariobruto <= 2500:
       salariodesc = salariobruto*0.1
if salariobruto > 2500:
     salariodesc = salariobruto*0.2

inss = salariobruto*0.10
fgts = salariobruto*0.11
totaldesc = inss+salariodesc
salarioliq = salariobruto - totaldesc



print(f'Salário Bruto:           :R${salariobruto}')
print(desconto_ir(salariobruto))
print(f'(-) INSS (10%)           :R${inss}')
print(f'FGTS (11%)               :R${fgts}')
print(f'Total de descontos       :R${totaldesc}')
print(f'Salário Líquido          :R${salarioliq}')
