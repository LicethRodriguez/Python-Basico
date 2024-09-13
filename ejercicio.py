# crear un menu con la condicional while de una calculadora

print(" Hola calculadora")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. Salir")
opcion = int(input("Digite la opcion del menu: "))
while opcion != 6:
    try:
        if opcion == 1:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1+num2
            print("el resultado de la suma es: ",resultado)
        elif opcion == 2:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1-num2
            print("el resultado de la resta es: ",resultado)
        elif opcion == 3:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1*num2
            print("el resultado de la multiplicación es: ",resultado)
        elif opcion == 4:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1/num2
            print("el resultado de la división es: ",resultado)
        elif opcion == 5:
            num1 = int(input("Digite el primer numero: "))
            num2 = int(input("Digite el segundo numero: "))
            resultado = num1**num2
            print("el resultado de la potencia es: ",resultado)
        elif opcion == 6:
            print ("salir")
        else:
            print("ERROR")

    except ValueError:
        print ("no funciona")

print ("Gracias por utlizar la calculadora")

