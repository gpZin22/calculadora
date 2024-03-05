n1 = int(input("insira o primeiro numero"))
n2 = int(input("insira o segundo numero"))


print("escolha as equações abaixo:")
print("1 - adição")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
operador = int(input("digite o numero correspondente"))

if operador == 1:
    print("o resultado da soma é: ", str (n1 + n2))
elif operador == 2:
    print("o resultado da subtracao é:", str (n1 - n2))
elif operador == 3:
    print("o resultado da multiplicação é:", str (n1 * n2))
elif operador == 4:
    print("o resultado da divisão é:", str (n1 / n2))
else:
    print("operador selecionado esta correto") 




