roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_num = input("Please Enter a Roman Number in uppercase: ")
deci_num = 0
i = 0

while i < len(roman_num):
    if i+1 < len(roman_num) and roman[roman_num[i]] < roman[roman_num[i+1]]:
        deci_num += roman[roman_num[i+1]] - roman[roman_num[i]]
        i+=2
    else:
        deci_num += roman[roman_num[i]]
        i+=1

print(deci_num)