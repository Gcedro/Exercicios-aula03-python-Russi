num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
op = input("Digite a operação (+ , -, *, /): ")

if op == "+":
    resultado = num1 + num2

elif op == "-":
    resultado = num1 - num2

elif op == "*":
    resultado = num1 * num2

elif op == "/":
    resultado = num1 / num2

else: 
    resultado = "Operação inválida"

print("Resultado", resultado)

