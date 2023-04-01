#Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input("Digite o valor do produto para calcular o desconto de 5%: R$ "))
print("O produto que custa R${:.2f}, com o desconto de 5%, passa a custar R${:.2f}" .format(preco, (preco -(preco*(5/100)))))
