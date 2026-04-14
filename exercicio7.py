ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = 2026 

idade = ano_atual - ano_nascimento

if idade < 16:
    print ("Não pode votar")

elif idade < 18:
    print ("Voto Opcional")

elif idade <70:
    print ("Voto Obrigatório")

else:
    print("Voto Opcional")