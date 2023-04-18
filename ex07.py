#
# autores:
# Cristiano e Michel

# data: 17/04/2023

# 7. 7.	Escreva um programa que peça a média de um aluno e a sua frequência 
# as aulas e verifique se esse aluno foi APROVADO, está em RECUPERAÇÃO, ou 
# foi RETIDO, para isso levando em consideração as seguintes situações:

# –	Um aluno qualquer só poderá ser aprovado se tiver a frequência mínima 
# às aulas de 75%; caso contrário, o aluno será reprovado por faltas;

# –	Um aluno qualquer também só poderá ser aprovado se tiver a média maior 
# igual a 70 pontos; caso contrário, o aluno poderá estar em recuperação 
# com média maior ou igual a 50 pontos; ou ainda está reprovado com média
# menor que 50 pontos;

# Solução 01:
media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite a frequência do aluno em %: "))

if frequencia < 75:
    print("Aluno REPROVADO por faltas.")
else:
    if media >= 70:
        print("Aluno APROVADO!")
    elif media >= 50:
        print("Aluno em RECUPERAÇÃO.")
    else:
        print("Aluno RETIDO por nota.")

# Solução 02:
media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

if frequencia >= 75:
    if media >= 70:
        print("Aluno APROVADO!")
    elif media >= 50:
        print("Aluno em RECUPERAÇÃO.")
    else:
        print("Aluno RETIDO por média.")
else:
    print("Aluno RETIDO por faltas.")

# Solução 03:
media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

if frequencia >= 75 and media >= 70:
    print("Aluno APROVADO!")
elif frequencia >= 75 and media >= 50:
    print("Aluno em RECUPERAÇÃO.")
else:
    print("Aluno RETIDO.")



