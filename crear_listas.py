#crear una lista
lista = [90, "L", "Liceth", False, 4.5]
print(f"los datos de la lista son: {lista}")
print (lista[2])
print(lista[-4])

#Recorrer una lista
print(lista [0:4])
print(lista[-1:])

#agregar datos a una lista 
numeros = [1,5]
numeros.append(100)
numeros.append("Rodriguez")
numeros.append("licethrodriguez2005@gmail.com")
numeros.append("1053329184")
print(numeros)

#tamaño lista
longitud = numeros.__len__()
print(f"el tamaño de la lista es: {longitud}")

#insert
numeros.insert(2, "Liceth")
print(numeros)
numeros.insert(1, "L")
print(numeros)

#reemplazar datos
numeros [-1] = "1054332598"
print(numeros)

#eliminar datos
numeros.remove (100)#elimina un elemento que deseemos
print(numeros)
numeros.pop()
print(numeros)#elimina ultimo elemento de la lista
numeros [2:4] = []
print(numeros)

#sacar datos de manera individual
for i in lista:
    print(f"datos lista: {i}")

#invertir lista
lista.reverse
print(lista)

#ordenar datos de una lista
x = [10, 2, 4, 5, 7, 8, 3]
print(sorted(x))

x.sort(reverse=True)
print(x)

X_total = sum (x)
print(f"la suma de la lista es: {X_total}")