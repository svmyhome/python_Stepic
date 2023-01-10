import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
file_name = 'numbers.json'
with open(file_name, 'w') as f:
    json.dump(numbers, f)

with open(file_name) as f:
    contain = json.load(f)
print(contain)


def favour_number():
    file_name = 'favourite_number.json'
    try:
        with open(file_name) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        n1 = input('Please type your favourite number : ')
        with open(file_name, 'w') as f:
            json.dump(n1, f)
    else:
        print(fav_num)

favour_number()