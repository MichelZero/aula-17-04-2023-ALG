#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# Escreva um programa que verifica se um número é múltiplo
# de 3 ou de 5 ou de ambos e imprime a mensagem correspondente.

numero = int(input("Digite um número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("O número é múltiplo de 3 e de 5.")
elif numero % 3 == 0:
    print("O número é múltiplo de 3.")
elif numero % 5 == 0:
    print("O número é múltiplo de 5.")
else:
    print("O número não é múltiplo de 3 nem de 5.")
