num_1 = int(input("Digite o primeiro número:"))
num_2 = int(input("Digite o segundo número:"))

if num_1 % num_2 == 0:
    print(f"{num_1} é divisível por {num_2}.")
else:
    print(f"{num_1} não é divisível por {num_2}.")