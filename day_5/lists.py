lista_vacia =  list()
lista5 = ["manzana", "agua", "película", "platano", "mamá"]
print(len(lista5))
print(lista5[0]+ " " +  lista5[2] +  " " + lista5[4])
mixed_data_types = ["Ángel" + "16" + "1.85" + "single" + "calle Marcelino Camacho"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print( it_companies)
print(len(it_companies))
print(f"{it_companies[0]} {it_companies[3]} {it_companies[6]}")
it_companies[3] = "Xiaomi"
print(it_companies)
it_companies.append("Acer")
print(it_companies)
it_companies.insert(4, "HP")
print(it_companies)
it_companies[1] = it_companies[1].upper()
print(it_companies)
print("#, ".join(it_companies))
print("Facebook" in it_companies)
it_companies.sort(reverse=False)
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[3:9])
print(it_companies[0:6])
print(it_companies[0:4]+ it_companies[5:9])
print(it_companies[1:])
it_companies4 = it_companies[:4]+ it_companies[5:]
print(it_companies4)
print(it_companies[:8])
print(it_companies.clear())
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_back = front_end + back_end
print(front_back)
full_stuck =front_back