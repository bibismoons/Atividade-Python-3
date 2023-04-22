num = int(input("Digite um número qualquer:"))
intervalo_inicial = int(input("Digite o valor inicial do intervalo:"))
intervalo_final = int(input("Digite o valor final do intervalo:"))

if intervalo_inicial <= num <= intervalo_final:
    print("O número está dentro do intervalo.")
else: 
    print("O número está fora do intervalo.")