def somaNum(num1, num2):
    return num1 + num2

def subtraiNum(num1, num2):
    return num1 - num2

def multiplicaNum(num1, num2):
    return num1 * num2

def divideNum(num1, num2):
    return num1 / num2

print("")
print("==Bem-vindo a calculadora simples em python==")

while True:
    print("")
    print("Diga que operação você quer fazer:")
    print("")
    print("Digite 1 para soma.")
    print("Digite 2 para subtração.")
    print("Digite 3 para multiplicação.")
    print("Digite 4 para divisão.")
    print("Digite 5 para sair.")

    print("")
    escolha = int(input())

    print("")
    if escolha in [1,2,3,4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("")
        if escolha == 1:
            #resultado = num1 + num2
            #print("Resultado: ", resultado)
            #print("Resultado: ", num1 + num2)
            print("Somando...")
            print(num1, " + ", num2, "= ", somaNum(num1, num2))
        elif escolha == 2:
            print("Subtraindo...")
            print(num1, " - ", num2, "= ", subtraiNum(num1, num2))
        elif escolha == 3:
            print("Multiplicando...")
            print(num1, " * ", num2, "= ", multiplicaNum(num1, num2))
        elif escolha == 4:
            print("Dividindo...")
            print(num1, " / ", num2, "= ", divideNum(num1, num2))
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("!!Você não digitou uma opção valida!!")
