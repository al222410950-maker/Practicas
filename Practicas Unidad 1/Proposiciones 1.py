n = int(input("¿Cuántas proposiciones quieres? "))
valores = [True, False]

encabezado = ""
for j in range(n):
    encabezado += chr(80 + j) + "\t"
print(encabezado)
print("-" * 25)

for i in range(2 ** n):
    fila = [(i >> (n - j - 1)) % 2 == 0 for j in range(n)]

    linea = ""
    for valor in fila:
        linea += str(valor) + "\t"
    print(linea)
