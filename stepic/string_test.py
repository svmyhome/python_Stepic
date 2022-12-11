sentence = "kdshjcj cdkscknm cdsnkcmkds"
print(sentence.title())
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
first_name = "ADA"
last_name = "LoVelaS"
FIO = f"{first_name} {last_name}"
message = f"Hello, {FIO.title()}"
print(message)
print('Hello')
print('\tHello')
print('jjgfhjghfj dkfdfjkd')
print('jjgfhjghfj \ndkfdfjkd')
print(' stip ', 'strip')
print(' stip '.rstrip(), 'strip')
print(' stip '.lstrip(), 'strip')
print(' stip '.strip(), 'strip')

string_world = 'Python is my second Language'
if 'my' in string_world:
    print('my')
else:
    print(f'This word do not contain my')

word_string = 'Python'
for i in range(-len(word_string), 0):
    print(word_string[i])
#
# st = input()
# sum = 'Цифр нет'
# for i in st:
#     if i in '0123456789':
#         sum = 'Цифра'
# print(sum)


print(word_string[1:4])
print(word_string[:4])
print(word_string[3:])
print(word_string[:6:2])
print(word_string[-1:-4])
print(word_string[-5:])
print(word_string[::-1])

word_string = word_string[:4] + 'X' + word_string[5:]
print(word_string)


s = 'toom om mo omom'
print(s.count('om', 0, 4)) # количество вхождение

s1 = 'foo'
s2 = 'bar'
print('foobar'.startswith(s1)) # начинается ли строка с, возвращает True|False
print('foobar'.startswith(s2))

print('foobar'.endswith(s1)) # заканчивается ли строка с, возвращает True|False
print('foobar'.endswith(s2))

print(s.find('om')) # ищет первое вхождение с начала
print(s.find('fom')) # если его нет то возвращает -1

print(s.rfind('om')) # ищет первое вхождение с конца
print(s.rfind('fom')) # если его нет то возвращает -1

s = '     foo bar foo baz foo qux      '
print(s.strip())

s = '     foo bar foo baz foo qux      '
print(s.lstrip())

s = '      foo bar foo baz foo qux      '
print(s.rstrip())

s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))


s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''

print(s1.isalnum()) # состоит ли исходная строка из буквенно-цифровых символов. Метод возвращает значение True
print(s2.isalnum())
print(s3.isalnum())

s1 = 'ABCabc'
s2 = 'abc123'
s3 = ''

print(s1.isalpha())  # состоит ли исходная строка из буквенных символов.
print(s2.isalpha())
print(s3.isalpha())


s1 = '1234567'
s2 = 'abc123'
s3 = ''

print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())

s1 = 'abc'
s2 = 'abc1$d'
s3 = 'Abc1$D'

print(s1.islower())
print(s2.islower())
print(s3.islower())

s1 = 'ABC'
s2 = 'ABC1$D'
s3 = 'Abc1$D'

print(s1.isupper())
print(s2.isupper())
print(s3.isupper())


s1 = '       '
s2 = 'abc1$d'

print(s1.isspace())
print(s2.isspace())

print(ord('A')) # определяет номер unicod
print(chr(66)) # определяет символ по номеру unicod

print('--------------------')

n1 = 14
s1 = "fsfftsfufksttskskt"
for i in s1:
    print(ord(i) - n1)
    #print(chr(ord(i) - n1), end="")