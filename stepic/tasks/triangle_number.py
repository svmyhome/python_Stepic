# 1
# 121
# 12321
# 1234321
# 123454321
# ...

k = int(input())
for j in range(1, k + 1):
    for i in range(j):
        print(i + 1, end="")
    for i in range(j - 2, -1, -1):
        print(i + 1, end="")
    print()
