cars_list = ["audi", "bmw", "toyota", "mersedes"]

for car in cars_list:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

for car in cars_list:
    if 1 < 2 and 2 < 3:
        print(cars_list[0].title())

print("bmw" in cars_list)
print("bmw1" in cars_list)
print("audi1" not in cars_list)

names = ["Nikolay", "Fedor"]
name = "Valdimir"
if name != names:
    print(f"{name} You may publish")

# age1 = 21
# if age1 < 4:
#     cost = 0
# elif age1 < 18:
#     cost = 25
# else:
#     cost = 40
# print(f'The price by ticket {cost}')

toppings = ["cheese", "mashrom", "onion"]

if "cheese" in toppings:
    print("cheese")
if "mashrom" in toppings:
    print("mashrom")
if "on" in toppings:
    print("onion")
print(f"You order is conteins")

age = 12
if age < 2:
    print("small baby")
elif age < 4:
    print("baby")
elif age < 13:
    print("teenager")
elif age < 20:
    print("old man")

fruits = ["cheese", "banana", "mashrom", "mellon", "onion"]

if "banana" in fruits:
    print("banana")
if "apple" in fruits:
    print("apple")
if "mellon" in fruits:
    print("mellon")
if "lime" in fruits:
    print("lime")
if "lime" in fruits:
    print("lime")

topping_list = ["onion", "cheese"]
if topping_list:
    for topping in topping_list:
        if "onion" == topping:
            print('Sorry, but this kind of topik doesn"t avalable')
        else:
            print(f"You chose {topping}")
else:
    print("You chose simple pizza")

users_list = []
if users_list:
    for user in users_list:
        if "admin" == user:
            print(f"Hello {user}? you have root accsess")
        else:
            print(f"{user} you have read/write access")
else:
    print("The user list is empty")

current_user = ["Vladimir", "andrey", "John"]
current_user_lower = [name.lower() for name in current_user]
new_user = ["Alex", "vladimir", "JOHN", "Mark"]
for user in new_user:
    if user.lower() in current_user_lower:
        print("You must chose new name")
    else:
        print("this name is avalaible")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers_list:
    if i == 1:
        print('1st')
    elif i ==2:
        print('2nd')
    elif i == 3:
        print('3rd')
    elif i > 3:
        print(f'{i}th')
