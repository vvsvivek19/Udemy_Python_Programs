flag = 0
s1 = input("Please enter first string: ")
s2 = input("Please enter second string: ")
if len(s1) == len(s2):
    for x in range(0, len(s1)):
        if s2.find(s1[x]) != -1:
            pass
        else:
            flag = 1
            break
else:
    flag = 1

if flag == 0:
    print("String is Anagram")
else:
    print("String is not anagram")
