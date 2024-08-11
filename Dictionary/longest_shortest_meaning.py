D1 = {'piece': 'a separate or limited portion or quantity of something',
      'patch': 'a small piece of material used to mend a tear or break, to cover a hole, or to',
      'area': 'any particular extent of space or surface',
      'visit': 'to go to see a person or place for a period of time',
      'with': 'in the company of somebody/something',
      'small': 'not large in size, number, amount, etc'}
largest = D1['piece']
smallest = D1['piece']
large_key = ''
small_key = ''
for x in D1:
    if len(D1[x]) >= len(largest):
        largest = D1[x]
        large_key = x
    if len(D1[x]) <= len(smallest):
        smallest = D1[x]
        small_key = x
print("'{}' has the largest meaning which is '{}'".format(large_key, D1[large_key]))
print("'{}' has the smallest meaning which is '{}'".format(small_key, D1[small_key]))
