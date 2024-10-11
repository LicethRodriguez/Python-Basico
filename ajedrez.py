tamaño = 8
tablero=[]
for fila in range (tamaño):
    filat=[]
    for columna in range(tamaño):
        if (fila+columna) % 2 ==0 :
            filat.append(1)
        else: 
            filat.append(0)
    tablero.append(filat)

for fila in tablero:
    print(fila)