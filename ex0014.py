#Escreva um programa que converte uma temperatura digitada em °C em °F

print('------------ CONVERSOR DE TEMPERATURA--------------')
celsius = float(input('Temperatura em °C: '))
print('{} °C, em Fahrenheit são {} °F' .format(celsius, (1.8*celsius+32)))
