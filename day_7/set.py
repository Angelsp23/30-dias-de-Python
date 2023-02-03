# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("Twirtter")
print(it_companies)
more_it_companies = {"Acer", "HP", "Xiomi"}
it_companies.update(more_it_companies)
print(it_companies)
it_companies.remove("HP")
print(it_companies)
print("la diferencia entre remove y discard es que si el elemento no existe, remove da error mientras que discard no")
C = A + B
print(C)
