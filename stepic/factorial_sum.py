"""
Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+\ldots+n!1!+2!+3!+…+n!.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значение суммы 1!+2!+3!+\ldots+n!1!+2!+3!+…+n!.

Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 11 до nn, то есть
n!=1\cdot2\cdot3\cdot…\cdot n
n!=1⋅2⋅3⋅…⋅n
"""
n = int(input())
sum = 0
for i in range(1, n + 1):
    counter = 1
    if i > 1:
        for j in range(1, i + 1):
            counter *= j
    else:
        counter *= int(i)
    sum += counter
print(sum)
