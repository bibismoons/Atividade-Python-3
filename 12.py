num = int(input("Digite um número:"))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} é múltiplo de 3 e de 5.")
elif num % 3 == 0:
    print(f"{num} é múltiplo de 3, mas não de 5.")
elif num % 5 == 0:
    print(f"{num} é múltiplo de 5, mas não de 3.")
else: 
    print(f"{num} não é múltilpo de 3 e nem de 5")