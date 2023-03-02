def suma(num1,num2):
    num3=num1+num2
    print(num3)
suma(3,4)

def area_of_circle(radio):
    area= radio**2 * 3.14159
    return area

print(area_of_circle(4))

def add_all_nums(*datos):
    total=0
    if not datos:
        print("no hay datos")
    else:
        for num in datos:
            total = total +num
    return total

"""     if type(datos)==int:
        total=sum(datos)
    else:
        print("no puedo sumar esos datos")
    return total  """

print(add_all_nums(3, 5, 8, 9))