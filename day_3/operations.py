age = int(16)
height = float(1.85)
ecuacion = complex= 3 + 3j
nbase =int(input("Area:"))
print(nbase)
altura =int(input("Altura:"))
print(altura)
print ("El perímetro de su triangulo es:")
print(0.5 * altura * nbase)

lado_a = int(input("Inserte lado a:"))
print(lado_a)
lado_b = int(input("Inserte lado b."))
print(lado_b)
lado_c = int(input("Inserte lado c:"))
print(lado_c)
perímetro = lado_a + lado_b + lado_c
print(f"Su perímetro es de: {perímetro}")

lenght = int(input("Inserte el largo:"))
print(lenght)
wide = int(input("Inserte el ancho:"))
print(wide)
area_rectangle = lenght*wide
perimeter_rectangle = 2*(lenght + wide)
print("su área es de:", area_rectangle)
print("su perímetro es de:", perimeter_rectangle)

pi=3,14
radio_circle= int(input("Inserte el radio:"))
print(radio_circle)
area_circle = pi * radio_circle**2
circum_circle = 2*pi*radio_circle
print(area_circle)
print(circum_circle)

funcion1="y=2x-2"
print("su función es:"+funcion1)
pendientef1= str(2)
print("su pendiente es:"+pendientef1)
interceptx= (2*0 -2)
print("el intercepto de x es:")
print(0,interceptx)
intercepty = (0+2)/2
print("el intercepto de y es:")
print(intercepty,0)

punto1=(2,2)
punto2=(6,10)
x1=2
x2=6 
y1=2
y2=10
m= (y2-y1)/(x2-x1)
print(f"su pendiente es:{m}")
euclideandistance= (x2-x1)**2 + (y2-y1)**2
print(f"la distancia eucliana es de: {euclideandistance}")

print(pendientef1==m)

numeros_prueba= (2,-3,4,5,6)
for n in numeros_prueba:
    print (n**2 + 6*n +9)

print(len("python"))
print(len("dragon"))
print(len("python")!=len("dragon"))

print("on"in "python")
print("on" in "dragon")
print("jargon" in "I hope this course is not full of jargon")
print("on" not in "dragon")
print("on" not in "python")
