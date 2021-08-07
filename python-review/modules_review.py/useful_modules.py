from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,8]

print(Counter(li)) # it creates a dictionary from the list that keeps track of how many times a number occur in the list

dictionary = defaultdict(lambda: 5,{'a': 1, 'b': 2}) # if the key doesn't exist it will return 5

print("default dict",dictionary['a']) #1
print("default dict",dictionary['c']) #5

# Ordered dictionary

d = OrderedDict()
d['a'] = 1
d['b'] = 1
d['c'] = 1
d['d'] = 1
