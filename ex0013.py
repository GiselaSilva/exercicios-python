#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Qual o salário do funcionário? R$ '))
print('O funcionário que recebia R$ {}, após o aumento de 15%, passsa a receber R$ {}' .format(salario, (salario + (salario*15/100))))
