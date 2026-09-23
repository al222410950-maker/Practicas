n = int(input("¿Cuántas proposiciones quieres? "))
valores = [True, False]

# Encabezado
encabezado = ""
for j in range(n):
    encabezado += chr(80 + j) + "\t"
encabezado += "¬P\tP∧Q\tP∨Q\tP→Q\tP↔Q"
print(encabezado)
print("-" * 70)

for i in range(2 ** n):
    fila = [(i >> (n - j - 1)) % 2 == 0 for j in range(n)]

    P = fila[0]
    Q = fila[1] if n > 1 else True

    negacion = not P
    conjuncion = P and Q
    disyuncion = P or Q
    condicional = (not P) or Q
    bicondicional = P == Q

    linea = ""
    for valor in fila:
        linea += str(valor) + "\t"
    linea += f"{negacion}\t{conjuncion}\t{disyuncion}\t{condicional}\t{bicondicional}"
    print(linea)