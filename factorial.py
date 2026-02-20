num = int(input("digite un numero para calcular su factorial: "))
factorial = 1

for x in range(1, num + 1):
    factorial = factorial * x

print(f"El factorial de {num} es {factorial}")