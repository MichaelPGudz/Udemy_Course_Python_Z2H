from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3]

print(Counter(mylist))

second_list = ['a', 'a', 10, 10, 10]

print(Counter(second_list))

print(Counter('aaaabbbshshhhshjxzc'))

sentence = "How many times does each word show up in this sentence with a word?"
print(Counter(sentence.lower().split()))

letters = 'aaaaaaaaabbbbbbbbcccccccccccddddddddddd'

c = Counter(letters)
print(c.most_common)

print(list(c))

# DEFAULT DICTIONARY
d = {'a': 10}
print(d['a'])

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])

d['Wrong key!']
print(d)

mytuple = (10, 20, 30)
mytuple[0]

dog = namedtuple('Dog', ['age', 'breed', 'name'])
rico = dog(age=5, breed='Husky', name='Rico')
print(type(rico))
print(rico)
print(rico.name)
print(rico[0])