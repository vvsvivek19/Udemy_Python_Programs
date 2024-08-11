s = input("Please enter a string: ")
punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
new_string = ''
for x in s:
    if x not in punc:
        new_string += x

print("New String:",new_string)
