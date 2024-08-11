def pascal(n):
    r = [1]
    tr = [0]
    print(r)
    for i in range(n-1):
        tr = [0] + r
        r = r + [0]
        nr = [x+y for x, y in zip(tr,r)]
        print(nr)
        r = nr
pascal(5)
