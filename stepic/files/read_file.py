with open('../text_files/print_file.txt') as file_object:
    content = file_object.read()
    print(content)
    print('=' * 10)

with open('../text_files/print_file.txt') as file_object:
    content1 = file_object.read()
    print(content1.rstrip())  # убирает новую строку после чтения файла
    print('=' * 10)

file_data = '../text_files/print_file.txt'

with open(file_data) as file_object:
    for line in file_object:
        print(line)
    print('=' * 10)

with open(file_data) as file_object:
    for line in file_object:
        print(line.rstrip())
    print('=' * 10)

resdlines_file = '../text_files/print_file.txt'
with open(resdlines_file) as file_object:
    list_lines = file_object.readlines()
for i in list_lines:
    print(i.rstrip())
print('+' * 10)

new_line = 'text_files/print_file.txt'
with open(new_line) as file_object:
    lines = file_object.readlines()
pi_str = ''
for line in lines:
    pi_str += line.strip()
print(pi_str)
print(len(pi_str))
print('-' * 10)
new_line1 = 'text_files/print_file.txt'
with open(new_line1) as file_object:
    lines = file_object.readlines()
pi_str1 = ''

for line in lines:
    pi_str1 += line.strip()
print(f'{pi_str1[:50]}')
print(len(pi_str1))
print('*' * 10)

new_line2 = 'text_files/print_file.txt'
with open(new_line2) as file_object:
    lines= file_object.readlines()
pi_str2 = ''
for line in lines:
    pi_str2 += line.strip()
birthday = input('Please type your birthday : ')
if birthday in pi_str2[:50]:
    print('Your birthday appears')
else:
    print('Your birthday does not appears')

new_line3 = 'text_files/new_txt.txt'
with open(new_line3) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

new_line4 = 'text_files/new_txt.txt'
with open(new_line4) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip().replace('Python', 'C++'))