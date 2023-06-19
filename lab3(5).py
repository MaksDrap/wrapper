import random
matrix = [[random.randint(-50, 50) for j in range(10)] for i in range(5)]
for row in matrix:
    print(row)
for j in range(10):
    pos = 0
    neg = 0
    for i in range(5):
        if matrix[i][j] > 0:
            pos += 1
        elif matrix[i][j] < 0:
            neg += 1
    if pos == neg:
        print("Cтовпчик з рівною кількістю додатних і від'ємних елементів:", j)
    else: print(0)