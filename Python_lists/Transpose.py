A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
T = []
for i in range(len(A[0])):
    S = []
    for j in range(len(A)):
        S.append(A[j][i])
    T.append(S)
print(T)