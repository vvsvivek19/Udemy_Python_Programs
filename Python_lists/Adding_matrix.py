A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
C = []

for i in range(len(A)):
    S = []
    for j in range(len(A[i])):
        S.append(A[i][j]+B[i][j])
    C.append(S)

print(C)
