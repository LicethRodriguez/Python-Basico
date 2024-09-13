#crear variables
num1 = 2
num2 = 5

#AND
print(num1 == num2 and num1 <= num2) # 1 1 -v
print(num1 == num2 and num1 > num2) # 1 0 -f
print(num1 < num2 and num1 > num2) # 0 0 -f
print(num1 < num2 and num1 >= num2) # 0 1 -f
#Ejemplo1
usuario = input("Digite el usuario: ")
contraseña = input("Digite la contraseña: ")
print(usuario== "LicethRodriguez" and contraseña == "123qwerty")

#OR
print(num1 == num2 or num1 <= num2) # 0 1 -v
print(num1 <= num2 or num1 > num2) # 1 0 -v
print(num1 > num2 or num1 > num2) # 0 0 -f
print(num1 > num2 or num1 >= num2) # 0 1 -f

#NOT
print(not True) #F
print(not False) #V
