with open('My.data','rb') as f:
    print(f.read(5).decode()) #reading two bytes from file
    f.seek(-3,1)
    print(f.read(1).decode())