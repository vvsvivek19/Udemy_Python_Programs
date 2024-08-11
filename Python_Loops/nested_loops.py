for i in range(0,5):
    for j in range(0,5):
        if i <= j:
            print("*", end=' ')
        else:
            print(' ', end=' ')
    print('')

S1 = 'abc'
S2 = 'xyz'
for i in S1:
    for j in S2:
        print(i,j,end=' ')
    print('')
