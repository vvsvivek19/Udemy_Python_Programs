flag = 0
def pangram_checker(s):
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    global flag
    for i in l:
        if i in s.lower():
            continue
        else:
            flag = 1
            break

S = input("Enter a string: ")
pangram_checker(S)

if flag == 0:
    print("String is Pangram")
else:
    print("String is not a Pangram")

