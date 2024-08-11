from datetime import *
time1 = datetime.now()
for i in range(0,1000000000):
    pass
time2 = datetime.now()
td = time2 - time1
print(td)