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
    return f"{fahrenheit}º"



def check_season(mes):
    str(mes)
    mes_capitalized=mes.capitalize()
    if mes_capitalized=="December" or mes_capitalized=="January" or mes_capitalized=="February":
        return  "It's Winter"
    elif mes_capitalized=="March" or mes_capitalized=="April" or mes_capitalized=="May":
        return "It's Spring"
    elif mes_capitalized=="June" or mes_capitalized=="July" or mes_capitalized=="August":
        return "It's Summer"
    elif mes_capitalized=="September" or mes_capitalized=="October" or mes_capitalized=="November":
        return "It's Autumn"
    else:
        return "es mal escrito, prube a escribirlo otra vez"



def print_list(*lista):
    for element in lista:
        print (element)


def reverse_list(array):
    list(array)
    array.reverse()
    return array
    

def capitalize_list_items(items):
    list(items)
    archivo=[]
    for r in items:
        str(r)
        r=r.capitalize()
        archivo.append(r)
    return archivo
        
def add_item(lista, cosa):
    list(lista)
    lista.append(cosa)
    return(lista)
      
def remove_item(lista, item):
    list(lista)
    lista.remove(item)
    return(lista)
    

def sum_of_numbers(numero):
    paquito=0
    for n in range(numero+1):
        paquito = paquito + n
    return paquito
    


print(sumadenumeros(3,4))
print(area_of_circle(4))
print(add_all_nums(5, 8, 9,"hola"))
print(convert_celsius_to_fahrenheit(20))
print(check_season("april"))
print_list("cebolla", "caramelo", "pimiento", "guayaba")
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]
print(capitalize_list_items(["apple", "watermelon", "melon"]))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

