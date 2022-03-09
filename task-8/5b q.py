X = [[10, 3, 5],
[7, 9, 2],
[11, 6, 9]]

Y = [[3, 5, 2, 9],
[7, 5, 3, 4],
[2, 7, 9, 7]]

result = [[sum(a*b for a,b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:

    print(r)

