def greet_user():
    """This is documentation of function"""
    print("Greeting You")


greet_user()


def greet_with_name(name: str):
    """This is documentation of function"""
    print(f"Greeting {name}")


greet_with_name("Vladimir")


def my_pets(name: str, animal_kind: str):
    """This is documentation of function"""
    print(f"I have a {animal_kind}. It's name {name}")


my_pets("willi", "horse")


def my_pets_indicate(name: str, animal_kind: str):
    """This is documentation of function"""
    print(f"I have a {animal_kind}. It's name {name}")


my_pets_indicate(animal_kind="horse", name="willi")


def my_pets_default(name: str, animal_kind="dog"):
    """This is documentation of function"""
    print(f"I have a {animal_kind}. It's name {name}")


my_pets_default(animal_kind="horse", name="willi")
my_pets_default(name="willi")


def t_short(size="L", text="Ilove"):
    print(f"The size {size} and text is {text}")


t_short()
t_short("M", "lkmvkmvfmklsvm")


def get_formated_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


print(get_formated_name(first_name="jimi", last_name="uuux"))


def get_all_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name


print(get_all_name(first_name="jimi", middle_name="antony", last_name="uuux"))
print(get_all_name(first_name="jimi", last_name="uuux"))


def person_inf(first_name, last_name, age=None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


person_obj = person_inf(first_name="Ivan", last_name="Ivanov")
print(person_obj)
print(person_obj.get("first"))
print(person_obj["last"])

person_obj1 = person_inf(first_name="Ivan1", last_name="Ivanov1", age=27)
print(person_obj1)
print(person_obj1.get("first"))
print(person_obj1["last"])
print(person_obj1.get("age"))


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


print(city_country(city="vologda", country="russia"))


def make_album(name_album, singer, tracks=None):
    album = {"album": name_album, "singer": singer}
    if tracks:
        album["number_tracks"] = tracks
    return album


alums = make_album(name_album="gold", singer="Cocker")
print(alums)
print(alums.get("album"))
print(alums.get("singer"))

alums1 = make_album(name_album="gold", singer="Cocker", tracks=39)
print(alums1)
print(alums1.get("album"))
print(alums1.get("singer"))
print(alums1.get("number_tracks"))

while True:
    print("For exit type q")
    album = input()
    if album == "q":
        break
    singer = input()
    if singer == "q":
        break
    tracks = input()
    if tracks == "q":
        break
    misic_project = make_album(name_album=album, singer=singer, tracks=tracks)
    print(misic_project)
    print(misic_project.get("album"))
    print(misic_project.get("singer"))
    print(misic_project.get("number_tracks"))

messages_list = [
    "vdsvdf",
    "vdfvdf vfdvdf",
    "vevmkdm kmrkmvdlm329uru",
    "kmvfd vfdjnvjfn",
]

new_message_list = []


def print_messages(messages_list, new_message_list):
    while messages_list:
        message = messages_list.pop(0)
        new_message_list.append(message)
        print(f"This message {message} removed")


def print_newMessage(messages_list, new_message_list):
    for message in new_message_list:
        print(message)
    print(messages_list)
    print(new_message_list)


print_messages(messages_list, new_message_list)
print_newMessage(messages_list, new_message_list)


def print_text(size: int, *args, **kwargs):
    dict_all = kwargs
    print(size)
    print(args)  # print typle
    print(*args)  # print string
    print(kwargs)  # dictionary
    print("*" * 10)

    for ard in args:
        print(ard)
        dict_all[ard] = ard
    dict_all[size] = size
    return dict_all


print(print_text(21, "message", "kcmskcmd", type="peperoni1", kind="trololo1"))

import my_import

my_import.print_pizza()

from my_import1 import print_pizza1

print_pizza1()

from my_import2 import print_pizza1 as pz

pz()
