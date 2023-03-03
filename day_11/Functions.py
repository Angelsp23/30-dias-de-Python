from pdb import Pdb


def sumadenumeros(num1,num2):
    num3=num1+num2
    return num3


def area_of_circle(radio):
    area= radio**2 * 3.14159
    return area



def add_all_nums(*datos):
    total=0
    datos_tipos= type(datos)
    if not datos:
        print("no hay datos")
    else:
        for num in datos:
            if type(num)==str:
                total= "no puedo realizar una suma con strings"
                break
            else:
                total=total +num            
    return total



def convert_celsius_to_fahrenheit(grados):
    fahrenheit=(grados*9/5)+32
    print(f"{fahrenheit}º")



def check_season(mes):
    str(mes)
    mes_capitalized=mes.capitalize()
    if mes_capitalized=="December" or mes_capitalized=="January" or mes_capitalized=="February":
        print("It's Winter")
    elif mes_capitalized=="March" or mes_capitalized=="April" or mes_capitalized=="May":
        print("It's Spring")
    elif mes_capitalized=="June" or mes_capitalized=="July" or mes_capitalized=="August":
        print("It's Summer")
    elif mes_capitalized=="September" or mes_capitalized=="October" or mes_capitalized=="November":
        print("It's Autumn")
    else:
        print("es mal escrito, prube a escribirlo otra vez")



def print_list(*lista):
    for element in lista:
        print (element)


def reverse_list(array):
    list(array)
    array.reverse()
    print(array)



print(sumadenumeros(3,4))
print(area_of_circle(4))
print(add_all_nums(5, 8, 9,"hola"))
convert_celsius_to_fahrenheit(20)
check_season("april")
print_list("cebolla", "caramelo", "pimiento", "guayaba")
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]


