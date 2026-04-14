salario = float(input("Digite o salário: "))

if salario <= 280:
    percentual = 0.20

elif salario <= 700:
    percentual = 0.15

elif salario <= 1500:
    percentual = 0.10

elif salario >= 1500:
    percentual = 0.05

aumento = salario * percentual 
novo_salario = salario + aumento

print("Salário antes:" , salario)
print("Percentual aplicado:", percentual *100, "%")
print("Valor do aumento", aumento)
print("Novo salário", novo_salario)