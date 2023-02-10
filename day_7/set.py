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

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

ages_set = set(age)
print(len(age))
print(len(ages_set))
print(len(ages_set)>len(age))
print("""la diferencia entre string, list, tuple y set es que una string es una conjunto de caracteres que se declara entre comilla y son inmutables,
 la listas son un conjunto de string, integers, etc que son mutables, es decir, pueden cambiarse una vez declaradas y tienen orden. Sin embargo, las tuples son como las listas pero no 
 pueden cambiarse una vez declarados, y los sets no tienen orden.""")
teacher= "I am a teacher and I love to inspire and teach people."
words_teacher= set(teacher.split())
print(words_teacher )
print(len(words_teacher))