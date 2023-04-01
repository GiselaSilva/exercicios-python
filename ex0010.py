#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere o dólar a R$5,06 (31/03/2023)

dinheiro = float(input("Quanto você tem de dinheiro na sua conta? R$ "))
print("Com R${} é possível comprar US${:.2f}" .format(dinheiro, (dinheiro/5.06)))
