dog = dict()
dog["name"] = "Carlitos"
dog["age"] = "5 years"
dog["breed"] = "golden retriever"
dog["color"] = "clear brown"
dog["legs"] = "4"
print(dog)
student_dct = {

    "first_name":"Ángel",
    "last_name":"Sánchez",
    "gender":"man",
    "age":"16",
    "marital_status" : "in relationship",
    "skills" : ["run", "think", "sleep"],
    "country": "ESPAÑA",
    "city" : "Jerez de la Frontera",
    "addres" : {
        'street':'Marcelino Camacho',
        'zipcode':'11405'
        }

}
print(student_dct)
print(len(student_dct))
print(student_dct["skills"])
print(type(student_dct["skills"]))
student_dct["skills"].append("write")
student_dct["skills"].append("read")
print(student_dct)
keys = student_dct.keys
print(keys)
values = student_dct.values
print(values)
print(student_dct.items())
del student_dct["marital_status"]
print(student_dct)
del student_dct