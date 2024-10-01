#Desenvolva um programa que leia as duas notas de um aluno, calcule e
#mostre a sua média

prova = float(input("digite a nota da prova"))
trabalho = float(input("digite a nota do trabalho"))


nota = (prova+trabalho)/2

print(f"sua nota é {nota}")

if nota<5: 
    print("hahahahahahaha, ficou com nota vermelha BURRO DEMAIS")
elif nota == 10:
    print("PARABÉNS")
    
else: print(":>")
