active = True
message = ""
while active:
    message = input("Input te text ")
    if message == "quit":
        active = False
    else:
        print(message)

while True:
    message = input('Input city ')
    if message == 'quit':
        break
    else:
        print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

confirmed_users = []
unconfirmed_users = ['Tina', 'Anny', "Mikle"]

while unconfirmed_users:
    user = unconfirmed_users.pop(0)
    confirmed_users.append(user)
for user in confirmed_users:
    print(user)

not_double_users = ['Tina', 'Mikle', 'Antony', 'Mikle', 'Mikle', 'Mikle', 'Anny', "Mikle"]
print(not_double_users)
while 'Mikle' in not_double_users:
    not_double_users.remove('Mikle')
print(not_double_users)

active = True
response = {}
while active:
    name = input('Type name ')
    message = input('Enter message ')
    response[name] = message
    again = input("AGAIN ? yes\\no ")
    if again == 'no':
        break
print(response)