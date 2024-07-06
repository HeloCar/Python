def eh_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b >= c or a + c >= b or b + c >= a:
        return True
    return False

lado1 = float(input('Insira o valor:\n'))
lado2 = float(input('Insira o valor:\n'))
lado3 = float(input('Insira o valor:\n'))

if eh_triangulo(lado1, lado2, lado3):
    print("Os lados informados podem formar um triângulo")
    if lado1 == lado2 == lado3:
        print('É um tirângulo equilátero')
    elif lado1 != lado2 != lado3:
        print('E um triângulo escaleno')    
    elif lado1 != lado2 or lado1 != lado3 or lado2 != lado3:
        if lado1 == lado3 or lado1 == lado2 or lado3 == lado2:
           print('É um triângulo isóceles')
else:
    print("Os lados informados não podem formar um triângulo")

