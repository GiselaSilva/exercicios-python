#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60,00 por dia e R$0,15 por Km rodado

dia = int(input('Por quantos dias deseja alugar o carro? '))
km = float(input('Quantos Km vai percorrer com o carro? '))
print('O total a pagar pelo aluguel é de R$ {:.2f}' .format((dia*60)+(km*0.15)))

