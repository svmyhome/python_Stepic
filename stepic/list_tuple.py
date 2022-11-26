"""
List commands:
words = []
words = ["word_1", "word_2", "word_3", "word_4"]
words[3] = 'word'
word.append() = 'last word'
word.insert(1, 'word)
del words[3]
word = words.pop(2) # may save and use
word = words.remove('word')
len(motos_peoples)
sorted(motos_peoples) #doesn't modify the original list
sorted(motos_peoples, reverse=True) #doesn't modify the original list
motos_peoples.sort() #modify the original list
motos_peoples.sort(reverse=True) #modify the original list
"""

words = ["word_1", "word_2", "word_3", "word_4"]
print(words)
print(words[1])
print(words[1].title())
print(words[-1].title())  # last digit
print(words[-2].title())
print(f"This is {words[2].title()}")

bikes = []
bikes.append("honda")
print(bikes)
bikes.append("ducati")
print(bikes)
bikes[1] = "suzuki"
print(bikes)
bikes.insert(1, "ducati")
print(bikes)
del bikes[1]
print(bikes)
bikes.append("ducati")
moto_last = bikes.pop()
print(moto_last)
print(bikes)
bikes.append("ducati")
moto_two = bikes.pop(1)
print(moto_two.title(), bikes)
bikes.remove("honda")
print(bikes)
print("=" * 50)
people = ["Jonn", "Mark", "Igor"]
print(people)
people[-1] = "Antony"
print(f'I"ll be glad to see you {people[0].title()}')
print(f'I"ll be glad to see you {people[1].title()}')
print(f'I"ll be glad to see you {people[2].title()}')

motos_peoples = ["honda", "ducati", "suzuki", "Jonn", "Mark", "Igor"]
print(len(motos_peoples))
print(motos_peoples)
print(sorted(motos_peoples))
print(sorted(motos_peoples, reverse=True))
print(motos_peoples)
print("-" * 30)
motos_peoples.reverse()
print(motos_peoples)
motos_peoples.reverse()
print(motos_peoples)
print("--Sort" * 15)
print(motos_peoples)
motos_peoples.sort()
print(motos_peoples)

magicans = ["Tom", "Alice", "Yan"]
for magican in magicans:
    print(f"{magican} the best magican in the world")
    print(f"Yeeee\n")


my_friends = ["Andey", "Evgeniy", "Vadim", "Daniil"]
for friend in my_friends:
    print(f"The name of my fiend is {friend}")
print("These are my best friends")

for index in range(6):
    print(index, end=" ")
print()
for index in range(1, 6):
    print(index, end=" ")
print()
for index in range(2, 25, 2):
    print(index, end=" ")
print()
list_numbers = list(range(2, 25, 2))
print(list_numbers)
print(f"The minimum number from the list is : {min(list_numbers)}")
print(f"The maximum number from the list is  : {max(list_numbers)}")
print(f"The sum of the numbers is : {sum(list_numbers)}")

squares = []
for index in range(1, 8):
    squares.append(index**2)
print(squares)

squares_list_comprehension = [index**2 for index in range(1, 8)]
print(squares_list_comprehension)

list_million = list(range(1, 1_000_001))
for index in list_million:
    print(index)
list_comprehension_million = [index for index in range(1, 1_000_001)]
print(list_comprehension_million)
print(min(list_million))
print(max(list_comprehension_million))
print(sum(list_comprehension_million))

for index in range(2, 20, 2):
    print(index)

for index in range(3, 30, 3):
    print(index)

list_cub = [index**3 for index in range(1, 11)]
for index in list_cub:
    print(index)

list_names = ["John", "Vadim", "Andrey", "Evgeniy", "Nikolay", "Tolik"]
print(list_names[1:3])
print(list_names[:3])
print(list_names[1:])
print(list_names[-3:])
for name in list_names[-4:]:
    print(name)
names_comprehentions = [name for name in list_names[-3:]]
print(names_comprehentions)

my_food = ['Lemon', 'Cream soup', 'Tomato']
his_food = my_food[:]
my_food.append('apple')
his_food.append('bananna')
for index in my_food:
    print(index)
for index in his_food:
    print(index)

menu = ('pizza', 'pasta', 'soup', 'potatoes')
for index in menu:
    print(index)
print(menu[0])
print(menu[1])
menu = ('pizza', 'ice cream', 'cola', 'potatoes')
for index in menu:
    print(index)