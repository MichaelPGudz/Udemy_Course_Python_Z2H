#Default Dictonary

from collections import defaultdict

d = {'k1':1}

d['k1']

d = defaultdict(object)

d['one']

for item in d:
    print(item)

d = defaultdict(lambda: 0)

print(d['one'])
d['two'] = 2
print(d['two'])

print(d)