from collections import Counter
import re
text = '''Python is an easy programming language. Python syntax is like the English language. 
Python language is easy to learn and adapt to compared with Java and C++. 
In Python language, the same task can be performed using fewer lines of code. 
Its easy to learn and easy to code.'''

words = re.findall('\w+', text)
print(words)
c = Counter(words)
print(c)
print( c.most_common(3))
