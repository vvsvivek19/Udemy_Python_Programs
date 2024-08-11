def fun2(*args):
    print(args)

L1 = [11,22,33]
fun2(L1[0],L1[1],L1[2])
fun2(*L1)
T1 = (10,20,30)
fun2(*T1)
name = "SKY"
fun2(*name)
name = "VIVEK"
fun2(*name)


'''
def fun1(*args, a,b):
    print(a,b,args)

fun1(44,55,66,77,a=22,b=33)
'''
