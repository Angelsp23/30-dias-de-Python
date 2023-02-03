vacio = ()
brothers = ("Guille", "Arabaneh", "Facundo" , "Mohamed")
sisters = ("Lucía", "Consu", "María de las Piedades", "Amarguras")
siblings = brothers + sisters
print(brothers)
print(sisters)
print(siblings)
print(len(siblings))
parents=("Inma", "Pepe")
family_members=siblings + parents
print(family_members)
sinblings = family_members[0:8]
print(siblings)
parents= family_members[8:10]
print(parents)
fruits= ("apple", "banana", "orange", "coco")
vegetables=("carrot", "pepper", "onion", "letuce")
animals=("bear", "lion", "tiger", "pig")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)
food_stuff_ls = list(food_stuff_tp)
print(food_stuff_ls)
print(food_stuff_ls[5:7])
print(food_stuff_ls[0:3] + food_stuff_ls[9:12])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
