#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 3. Escreva um programa que verifica se uma pessoa pode votar ou
# não com base em sua idade e imprime a mensagem correspondente.

idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("Você pode votar.")
else:
    print("Você ainda não pode votar.")
