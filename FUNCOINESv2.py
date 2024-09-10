print("mas sobre funciones ")
# aqui se escirben las funciones 
def suma_ab(a,b):
    s=a+b
    return s
def resta_ab(a1,b2):
    s1=a1-b2
    return s1
def multiplicacion_ab(a5,b6):
    s3=a5*b6
    return s3
def division_ab(a3,b4):
    s2=a3/b4
    return s2
# llamar la funcion 
print("calculando suma")
n1=float(input("ingresa el primer numero para suma "))
n2=float(input("ingresa el segundo numero para suma "))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")

print("_______________________________________")

print("calculando resta")
n3=float(input("ingresa el primer numero para restar "))
n4=float(input("ingresa el segundo numero para restar "))
resta=resta_ab(n3,n4)
print(f"la resta de {n3} - {n4} es {resta}")

print("_______________________________________")

print("calculando multiplicacion")
n5=float(input("ingresa el primer numero para multiplicar "))
n6=float(input("ingresa el segundo numero para multiplicar "))
multiplicacion=multiplicacion_ab(n5,n6)
print(f"la multiplicacion de {n5} * {n6} es {multiplicacion}")

print("_______________________________________")

print("calculando division")
n7=int(input("ingresa el primer numero para dividir "))
n8=int(input("ingresa el segundo numero para dividir "))
division=division_ab(n7,n8)
print(f"la dicvision de {n7} / {n8} es {division}")