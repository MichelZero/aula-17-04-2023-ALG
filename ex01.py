#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 1.	Escreva um programa que verifica se um número é positivo, 
# negativo ou zero e imprime a mensagem correspondente.

numero = float(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
