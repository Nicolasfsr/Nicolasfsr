a = int(input("Digite un numero"))
b = int(input("Digite otro  numero"))
c = int(input("Digite orto  numero"))

if a == b and b == c:
    print("Los tres numeros son iguales")

elif a == b  or a == c or c == b:
    print("Hay dos iguales")
else:
    print("Son distintos")
