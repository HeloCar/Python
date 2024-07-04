nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))
media = (nota1+nota2)/2
conceito = str
situacao = str

if media < 4:
    if media >= 0:
        conceito = 'E'
        situacao = 'REPROVADO'
if media < 6:
    if media >= 4:
        conceito = 'D'
        situacao = 'REPROVADO'
if media < 7.5:
    if media >= 6:
        conceito = 'C'
        situacao = 'APROVADO'
if media < 9:
    if media >= 7.5:
        conceito = 'B'
        situacao = 'APROVADO'
if media <= 10:
    if media >= 9:
        conceito = 'A'
        situacao = 'APROVADO'

print(f'1ª nota: {nota1}')
print(f'2ª nota: {nota2}')
print(f'Média: {media}')
print(f'Conceito: {conceito}')
print(f'Situação do aluno: {situacao}')