# lst, lst Comprehension, Tuple

#lst

# Creating empty list
lst_1 = []
lst_2 = list()

# Creating the list with values
lst_1 = ["word_1", "word_2", "word_3", "word_4"] # ['word_1', 'word_2', 'word_3', 'word_4']
lst_2 = list("word_1") # ['w', 'o', 'r', 'd', '_', '1']

# Adding values to the list
lst_1[3] = 'word'
lst_2.append('last word') #the element is added to the last position
lst_1.insert(1, 'word') #the element is added to specific position
lst_1[3] = 'word'

# Join list
print([1, 2, 3, 4] + [5, 6, 7, 8])
print([7, 8] * 3)
print([0] * 10)

lst_1 = [1]
lst_2 = [3, 4, 5]
lst_1.extend(lst_2) # The second list is added to first list
print(lst_1)

# Deleting an item in the list
del lst_1[3] # element is deleted by specific index
delet_elem = lst_1.pop()  # last element is removed and we can use it
element_1 = lst_1.pop(2) # a specific element is removed and we can use it
lst_1.remove('word') # remove by name, only first element is removed
lst_1.remove(True) # [1, True, 0, False] Also 1 = True and 0 = False

# Sorting items in a list
cars = ['bmw', 'toyota', 'volvo']
cars.sort() # the original list is sorted and modified
cars.sort(reverse=True) # the original list is sorted and modified

sorted(cars) # the original list is sorted but not changed
sorted(cars, reverse=True) # the original list is sorted but not changed
sorted_lst = sorted(cars)

cars.reverse() # с#the original list is reversed and modified
print(cars)

# Working with elements in List

len(lst_1) # length the list

magicans = ["Tom", "Alice", "Yan"]
for item in lst_1:  # overshoot
    print(f"{item} the best magican in the world")

min(lst_1)
max(lst_1)
sum(lst_1)

lst_1.count(1) # count
lst_1.index(1) # output value
lst_1.index(1, 3) # output value


# Copying a List
b_1 = lst_1.copy()
с_1 = lst_1[:]
c_2 = list(lst_1)


# List comprehension

squares_list_comprehension = [index**2 for index in range(1, 8)]
# [1,2,3,4,5,6,7]

numbers = [i for i in range(10)]
# [0,1,2,3,4,5,6,7,8,9]
chars = [c for c in 'abcdefg']
# ['a','b','c','d','e','f','g']

n = int(input())
lines = [input() for _ in range(n)]

lines = [input() for _ in range(int(input()))]


numbers = [int(input()) for _ in range(int(input()))]

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
lst_numbers = list(range(2, 25, 2))
print(lst_numbers)
print(f"The minimum number from the lst is : {min(lst_numbers)}")
print(f"The maximum number from the lst is  : {max(lst_numbers)}")
print(f"The sum of the numbers is : {sum(lst_numbers)}")

squares = []
for index in range(1, 8):
    squares.append(index**2)
print(squares)

squares_lst_comprehension = [index**2 for index in range(1, 8)]
print(squares_lst_comprehension)

lst_million = list(range(1, 1_000_001))
for index in lst_million:
    print(index)
lst_comprehension_million = [index for index in range(1, 1_000_001)]
print(lst_comprehension_million)
print(min(lst_million))
print(max(lst_comprehension_million))
print(sum(lst_comprehension_million))

for index in range(2, 20, 2):
    print(index)

for index in range(3, 30, 3):
    print(index)

lst_cub = [index**3 for index in range(1, 11)]
for index in lst_cub:
    print(index)

lst_names = ["John", "Vadim", "Andrey", "Evgeniy", "Nikolay", "Tolik"]
print(lst_names[1:3])
print(lst_names[:3])
print(lst_names[1:])
print(lst_names[-3:])
for name in lst_names[-4:]:
    print(name)
names_comprehentions = [name for name in lst_names[-3:]]
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