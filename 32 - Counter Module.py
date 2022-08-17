#Counter

from collections import Counter

l = [1,1,1,1,12,2,2,2,2,2,3,3,3,3,4,4,5,5,5]

print(Counter(l))

s = 'asssssssssssvaavaaaaaaaaavavavababasbsbsba'

print(Counter(s))

s = 'How many times does each word show up in this sentence word word show up up ay ay ay'

words=s.split()

print(Counter(words))

c = Counter(words)

print(c.most_common(2))

print(sum(c.values()))