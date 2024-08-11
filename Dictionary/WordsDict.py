D1 = {'piece': 'a separate or limited portion or quantity of something',
      'patch': 'a small piece of material used to mend a tear or break, to cover a hole, or to',
      'area': 'any particular extent of space or surface',
      'visit': 'to go to see a person or place for a period of time',
      'with': 'in the company of somebody/something',
      'small': 'not large in size, number, amount, etc'}

keys = list(D1.keys())
values = list(D1.values())
lens = [len(x) for x in values]
# for x in values:
#     lens.append(len(x))

max_mean = max(lens)
min_mean = min(lens)

max_index = lens.index(max_mean)
min_index = lens.index(min_mean)

print("Largest word is '{}' and its meaning is '{}'.".format(keys[max_index],values[max_index]))
print("Smallest word is '{}' and its meaning is '{}'.".format(keys[min_index],values[min_index]))
