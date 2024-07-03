a = float(input('Insira o valor do seu salário bruto '))
b = a*0.11
c = a*0.08
d = a*0.05
e = a - b - c -d

print('+ Salário Bruto : R$', a)
print('- IR (11%) : R$', b)
print('- INSS(8%) : R$', c)
print('- Sindicato : R$', d)
print('= Salário Líquido : R$', e)