#Estructura de repetición FOR
 
for i in range (5):
    print(f"su dato es:{i}")

for i in range (0,5):
    print(f"su dato es:{i}")

for i in range (20,101): 
    print(f"su dato es:{i}")

for i in range (0,11):
    print(f"su dato es:{i}")

for letra in "Python":
    print(letra)

#Ejemplo1
cadena = "Programacion"
for letra in cadena: 
    if letra == "r":
        print("Se encontro una r")
        break 
    else:
        print("letra no encontrada")
print("esta por fuera del ciclo")

#tabla 2
for i in range (1,13):
    print(f"2X{i}={2*i}")

