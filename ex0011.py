#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
#de tinta pinta uma área de 2.0m2

larg = float(input("Qual a largura da parede em metros(m): "))
comp = float(input("Qual o comprimento da parede em metros(m): "))
area = larg*comp
print("A área a ser pintada é de {} m2" .format(area))
print("A quantidade de tinta necessária para pintar {}m2 é de {}l" .format(area, (area/2)))
