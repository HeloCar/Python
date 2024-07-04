salario = float(input('Informe o salário do colaborador: '))

def percentual_salario(salario):
     if salario <= 280:
          salario = 20
     if salario >= 281:
         if salario <= 700:
             salario = 15
     if salario >= 701:
         if salario <= 1500:
             salario = 10
     if salario >= 1501: 
         salario = 5
     return(f'O percentual é de {salario}%')

def valor_aumento(salario):
     if salario <= 280:
         salario = salario*0.20
     if 281 <= salario:
         if salario <= 700:
             salario = salario*0.15
     if 701 <= salario:
         if salario <= 1500:
             salario = salario*0.10
     if salario >= 1501:
         salario = salario*0.05

     return(f'O aumento é de: R${salario}')

     
def reajuste_salario(salario):
     if salario <= 280:
         salarionovo = salario*1.20
     if 281 <= salario:
         if salario <= 700:
             salarionovo = salario*1.15
     if salario >= 701:
         if salario <= 1500:
             salarionovo = salario*1.10
     if salario >= 1501:
         salarionovo = salario*1.05

     return(f'Salário após o reajuste: R${salarionovo}')


print(f'Salário antes do reajuste: R${salario}')
print(percentual_salario(salario))
print(valor_aumento(salario))
print(reajuste_salario(salario))