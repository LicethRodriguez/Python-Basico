#Declarar una matriz se le da el nombre 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz2= [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
#recorrer matriz
for fi in matriz:
    for co in fi:
        print(f"elementos matriz: {co}, {fi}")
matriz3 = [
    ["a", "b", "c", "d", "e","f"],
    [46678575, 1052338581, 1053329184, 7309343, 4658921, 1052324581],
    ["liceth", "rodriguez", "dario", "julio", "dayana", "leidy"],
    [12, 13, 14, 15, 20, 26],
]
for fi in matriz3:
    for co in fi:
        print(f"elementos matriz: {co}")
#tamaño matriz
f = len(matriz3)
print(f"tamaño filas {f}")
c = len(matriz3[2])
print(f"tamaño columnas {c}")

#recorre filas con metodo range
for i in range (f):
    for j in range(c):
        print(f"posicion {i},{j}: {matriz2[i][j]}")

print(matriz[1][2])