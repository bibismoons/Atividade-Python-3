num = int(input("Digite um número:"))
divisores = []

for i in range (1, num + 1):
    if num % i == 0:
        divisores.append(i)
        
if len(divisores) == 2:
    print(f"{num} é um número primo.")
    print(f"Divisores: {divisores}")
else:
    print(f"{num} não é um número primo.")
    