age = int(input("insert your age "))
if age>=18:
    print("You are old enough to drive")
else:
    print(f"You need {18-age} more years to learn to drive")

years = int(input("enter your age "))
if years>16:
    print(f"You are {years-16} older than me")
    if years-16 <= 2:
        print(f"You are a little older than me, only {years-16}")
elif years==16:
    print("we are 16 both")
else:
    print(f"I'm {16-years} older than you")

a = int(input("Enter a random number: "))
b = int(input("Enter another number: "))
if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

grade = int(input("Enter your high school scores: "))
if grade >= 80:
    print("Your grade is A")
if grade>=70 and grade <80:
    print("Your grade is B")
if grade >=60 and grade <70:
    print("Your grade is C")
if grade >=50 and grade <60:
    print("Your mark is D")
if grade <50:
    print("Your mark is F")

month = str(input("Enter the month (in English): "))
month_capitalized = month.capitalize()
if month_capitalized== "October" or month_capitalized=="November" or month_capitalized=="September":
    print("we are in Autumn")
if month_capitalized=="January" or month_capitalized=="December" or month_capitalized=="February":
    print("we are in winter")
if month_capitalized== "March" or month_capitalized=="April" or month_capitalized=="May":
    print("we are in Spring")
if month_capitalized=="June" or month_capitalized=="July" or month_capitalized=="August":
    print("we are in Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit= input("Enter a fruit: ")
if new_fruit not in fruits:
    fruits.append(new_fruit)
    print(fruits)
else:
    print("That fruit already exist in the list")


