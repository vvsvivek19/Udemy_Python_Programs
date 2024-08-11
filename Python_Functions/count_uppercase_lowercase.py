def count(s):
    uppercase_count = 0
    lowercase_count = 0
    for i in s:
        if i.isupper():
            uppercase_count += 1
        elif i.islower():
            lowercase_count += 1
    return uppercase_count, lowercase_count


S = input("Please enter a string: ")
UC, LC = count(S)
print("Uppercase count:", UC)
print("Lowercase count:", LC)
