#faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo de
#cada litro de tinta, pinta uma área de 2m2.
#area = largura*altura tinta tinta= area/2


largura = float(input("Digite o largura da parede"))
altura = float(input("Digite a altura da parede"))


area = largura*altura 

tinta = area / 2

print(f"para uma parede de area {area}, voce vai precisar de {tinta} litro de tinta")