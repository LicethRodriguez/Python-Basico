opcion = (input("Digite la opción del menu: "))
resultado = 1+2
while opcion != "salir":
    if opcion == "1":
        print (f"suma= {resultado}")
    elif opcion =="2":
        print("resta=",3-4)   
    elif opcion == "3":
        print("multiplicación=", 3*4) 
    elif opcion == "4":
        print("división=", 3/4) 
    elif opcion == "5":
        print("potencia=", 3**4) 
    else: 
        print ("opcion incorrecta, ingrese del 1 al 5")
print("fuera del bucle") 