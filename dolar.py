#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (Consultar o valor do Dólar)

carteira = float(input("quanto voce tem na sua conta bancaria?"))

dolares = carteira/5.45

print(f"voce pode comprar {dolares}")

if dolares<100: print("hahahahahaha")