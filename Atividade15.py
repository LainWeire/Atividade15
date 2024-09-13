# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

op = (input("Que operação deseja fazer entre soma, subtração, multiplicação e divisão? "))
n1 = float(input("digite o primeiro número. "))
n2 = float(input("digite o segundo número. "))


if (op == "subtração"):
    print (n1 - n2)

elif (op == "soma"):
    print (n1 + n2)

elif (op == "divião"):
    print (n1 // 2)

elif (op = "multiplicação"):
    print (n1 * n2)

else:
    print("Inválido.")