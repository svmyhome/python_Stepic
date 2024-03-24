A = 1
B = A
print(f"A and B are references to the same object A = {id(A)}, B = {id(B)}")

C = 2
D = 3
print(f"C and D are references to the different object C = {id(C)}, D = {id(D)}")

C, D = D, C
print(f"The references changed C = {id(C)}, D = {id(D)}")


print(2 + 3)
print(4 / 2)
print(1000000)
print(1_000_000)

THIS_IS_CONST = 1000
print(THIS_IS_CONST)


# input values

s1, s2 = input().split()
print(s1, s2)

s3, s4 = map(str.strip, input().split())
print(s1, s2)

lst = map(str.strip, input().split())
print(lst)
