def create_cubes(n):
    result = []
    for x in range(n):
         result.append(x**3)
    return result

def create_cubes(n):

    for x in range(n):
         yield x**3

for x in create_cubes(10):
    print(x)

def gen_fibon(n):

    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b,a+b

for number in gen_fibon(10):
    print(f"Fibon: {number}")

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
# print(next(g))

s = "hello"

for letter in s:
    print(letter)

s_iter = iter(s)

next(iter(s))
next(iter(s))
next(iter(s))
next(iter(s))
next(iter(s))
