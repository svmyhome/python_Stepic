A = 1
B = A
print(f'A and B are references to the same object A = {id(A)}, B = {id(B)}')

C = 2
D = 3
print(f'C and D are references to the different object C = {id(C)}, D = {id(D)}')

C, D = D, C
print(f'The references changed C = {id(C)}, D = {id(D)}')
