def generate_squares(n):

    for num in range(n):
        yield num**2

for number in generate_squares(10):
    print(number)

import random


def rand_num(low,high,n):

    for number in range(n):
        num = random.randint(low, high)
        yield num


for num in rand_num(1,10,12):
    print(num)

s = 'hello'
s_iterated = iter(s)
print(next(s_iterated))

#I would use a generator with yield statemenet istead of return in case I did not want to save the output of the iteration and also to save the memory.

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

