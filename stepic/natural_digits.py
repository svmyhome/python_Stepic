"""
На вход программе подается два натуральных числа aa и bb (a < ba< b).
Напишите программу, которая находит все простые числа от aa до bb включительно.
"""
n1, n2 = int(input()), int(input())
for i in range(n1, n2 + 1):
    counter = 1
    count_number = 0
    while counter <= n2:
        if i % counter == 0:
            count_number += 1
            counter += 1
        else:
            counter += 1
    if count_number == 2:
        print(i)