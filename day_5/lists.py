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