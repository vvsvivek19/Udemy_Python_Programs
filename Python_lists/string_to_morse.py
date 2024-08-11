morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....','..', '.---']
message = 'deface'
code = []
for x in message:
    index = ord(x) - ord('a')
    code.append(morse[index])
print("Morse Code for deface is:",code)

