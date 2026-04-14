estado = int(input("Digite o código do estado (1 a 5): "))
peso_ton = float(input("Digite o peso da carga (em toneladas): "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

peso_kg = peso_ton * 1000

if 10 <= codigo_carga <= 20:
    preco_kg = 100.00
elif 21 <= codigo_carga <= 30:
    preco_kg = 250.00
else:  
    preco_kg = 340.00

preco_carga = peso_kg * preco_kg

if estado == 1:
    taxa = 0.35
elif estado == 2:
    taxa = 0.25
elif estado == 3:
    taxa = 0.15
elif estado == 4:
    taxa = 0.05
else:  
    taxa = 0

imposto = preco_carga * taxa

total = preco_carga + imposto

print(f"Peso em kg: {peso_kg:.2f}")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Total: R$ {total:.2f}")