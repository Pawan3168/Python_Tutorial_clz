# Multiplicaltion of two matrix
X = [[1,8,4],
    [4 ,5,6],
    [5 ,8,9]]

Y = [[15,8,3],
    [6,4,7],
    [4,6,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        # result[i][j]=0
        for k in range(len(Y)):
            result[i][j] = result[i][j] + X[i][k] * Y[k][j]
print(result)