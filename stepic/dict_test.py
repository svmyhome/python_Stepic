alien_0 = {"color": "green", "point": 5}
print(alien_0["color"])
print(alien_0["point"])
alien_0["x_coordinats"] = 150
alien_0["y_coordinates"] = 200
print(alien_0)

alien_1 = {}
print(alien_1)
alien_1["value_1"] = 1
print(alien_1)

alien_1["value_1"] = 2
print(alien_1)
alien_run = {"x_position": 1, "y_postion": 10, "speed": ""}
speed = 3
if speed == 1:
    alien_run["x_position"] += speed
elif speed == 2:
    alien_run["x_position"] += speed
elif speed == 3:
    alien_run["x_position"] += speed
print(alien_run)
del alien_run["speed"]
print(alien_run)
print(alien_1.get("value_3"))

my_dict = {
    "ivan": "first",
    "andrey": "second",
    "tom": "third",
    "tom1": "third",
    "Nik": "four",
    "jen": "five",
}
friends = ["andrey", "nik"]
print(my_dict["ivan"])
print(my_dict.get("andrey"))
for key, value in my_dict.items():
    print(f"Key is {key}, Value is {value}")

for key in my_dict.keys():
    print(f"Key is {key.title()}")
print("-" * 30)
for name in my_dict:
    print(f"Hi, {name.title()}")

    if name.lower() in friends:
        friend_numder = my_dict[name]
        print(f'Friend {name.title()} have the number "{friend_numder}"')
print("-" * 30)
for name in sorted(my_dict.keys()):
    print(name)
print("-" * 30)
for value in my_dict.values():
    print(value)
print("-" * 30)
for value in set(my_dict.values()):
    print(value)

rivers = {"nile": "egipt", "volga": "russia", "misissippi": "usa"}
for river, country in rivers.items():
    print(f"The river {river.title()} runs through {country.title()}")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

alien_0 = {"race": "ork", "color": "green"}
alien_1 = {"race": "elf", "color": "blue"}
alien_2 = {"race": "human", "color": "yellow"}

aliens = [alien_0, alien_1, alien_2]
for i in aliens:
    print(i)
print("-" * 30)
aliens_list = []

for i in range(30):
    aliens_list.append({"race": "ork", "color": "green"})

for i in aliens_list[:5]:
    print(i)

print(f"length {len(aliens_list)}")

for i in aliens_list[:3]:
    if i["color"] == "green":
        i["race"] = "eldar"
        i["color"] = "red"

for i in aliens_list[:5]:
    print(i)

pizza = {"type": "peprono", "topping": ["cheese", "tomato", "onion"]}

print(pizza["type"])
for topping in pizza["topping"]:
    print(topping)

favorite_language = {
    "cindy": ["C", "Java"],
    'norman': ['Python'],
    'joe': ['go', 'rubi', 'js']
}

for name, languages in favorite_language.items():
    print(f'{name.title()} like ')
    for language in languages:
        print(language.title())
    print()

users = {
    'petr': {'first' : 1, 'second': 2},
    'ivan': {'first': 3, 'second': 4}
}

for user, used_data in users.items():
    print(user)
    print(f"{used_data['first']} {used_data['second']}")