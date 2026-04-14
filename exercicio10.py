# Entrada
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# Colocar em ordem decrescente
lados = sorted([A, B, C], reverse=True)
A, B, C = lados

# Verifica se forma triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Tipo pelos ângulos
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    # Tipo pelos lados
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")