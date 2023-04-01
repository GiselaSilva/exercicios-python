#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média
#No terminal digitar a nota com ponto (.)

nota1 = float(input("Digite a nota do 1º semestre: "))
nota2 = float(input("Digite a nota do 2 semestre: "))
media = (nota1 + nota2)/2
print("A média entre {} e {} é {:.2f}" .format(nota1, nota2, media))
