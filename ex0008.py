#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
# 1m = 100cm // 1m = 1000mm

metros = float(input("Digite uma medida em metros(m): "))
print("A medida de {}m é igual a {}cm" .format(metros, (metros*100)))
print("A medida de {}m é igual a {}mm" .format(metros, (metros*1000)))
