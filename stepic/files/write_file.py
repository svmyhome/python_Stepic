new_file_1 = 'write_file_1.txt'
with open(new_file_1, 'w') as file_object:
    file_object.write('Hello Python1')

with open(new_file_1, 'w') as file_object:
    file_object.write('Hello Python1')
    file_object.write('Hello Python2')

with open(new_file_1, 'w') as file_object:
    file_object.write('Hello Python1\n')
    file_object.write('Hello Python2\n')

with open(new_file_1, 'a') as file_object:
    file_object.write('Hello Python3\n')
    file_object.write('Hello Python4\n')

file_name = 'guess_book.txt'

while True:
    name = input('Please type your name : ')
    with open(file_name, 'a') as file_object:
        file_object.write(f'{name}\n')
    print(f'Hello {name}')