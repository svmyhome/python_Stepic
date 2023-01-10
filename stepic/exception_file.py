try:
    print(5 / 0)
except ZeroDivisionError:
    print('You can"t  Division by zero')

# print('I can  divide, please type two numbers ')
# print('If you want stap , type q')
# while True:
#     num1 = input()
#     if num1 == 'q':
#         break
#     num2 = input()
#     if num2 == 'q':
#         break
#     try:
#         answer = int(num1) / int(num2)
#     except ZeroDivisionError:
#         print('You can"t divide by zero')
#     else:
#         print(answer)

file_name = 'alixe.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('File dos not exist')
else:
    words = content.split()
    print(f'In file {file_name} is contains {len(words)}')


def counter_word(file_name):
    try:
        with open(file_name, encoding='utf-8') as f:
            book = f.read()
    except FileNotFoundError:
        print(f'Book {file_name} does not exist')
    else:
        words = book.split()
        print(f'In book {file_name} has about {len(words)} words')


books = ['alixe.txt', 'alix3.txt', 'alixe_2.txt']

for book in books:
    counter_word(book)

n1 = 1
n2 = 'df'
try:
    answer = n1 + n2
except TypeError:
    print(' You numer is string')
else:
    print(answer)
