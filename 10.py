num = int(input("Digite um número inteiro positivo que seja maior que 1:"))

if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")
else:
    print("O número precisa ser positivo e maior que 1 para ser primo.")