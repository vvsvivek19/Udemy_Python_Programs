s = input("Please enter a string: ")
lower = ''
upper = ''
others = ''
for x in s:
    if x.islower():
        lower = lower + x
    elif x.isupper():
        upper = upper + x
    else:
        others = others + x
new_string = lower + upper + others
print("Rearranged String:",new_string)

