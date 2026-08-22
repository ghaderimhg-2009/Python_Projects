n = int (input())
x = int (input())

for i in range(n):
    if x % 2 == 0:
        x = x // 2
    else:
        x = 2 * x - 1
    print (x)