#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(type(nome))
print(nome, " é numérico?", nome.isnumeric())
print(nome, " é alfabético?", nome.isalpha())
print(nome, " é alfanumérico?", nome.isalnum())

print(type(idade))
print(idade, " é numérico?", idade.isnumeric())
print(idade, " é alfabético?", idade.isalpha())
print(idade, " é alfanumérico?", idade.isalnum())
