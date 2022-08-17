def myfunc(*args):
    return sum(args) *0.05

res = myfunc(10,20)
print(res)

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fuit here")

myfunc(fruit="Apple", veggie = "lettuce")

def myfunc(*args,**kwargs):

    print("I would like {} {}".format(args[0],kwargs["food"]))

myfunc(10,20,30,fruit="orange",food="eggs", animal="dog")


def myfunc(*args):
    list = []
    for i in args:
        if i%2==0:
            list.append(i)
    return list


x = myfunc(-4, 3, -1 , -2, 4, 2, 6, 20)
print(x)

def myfunc(string):
    x = 0
    a = ""
    for i in string:
        x += 1
        if x%2==0:
            y = i.upper()
        else:
           y = i.lower()
        a = a + y
    return a

b = myfunc("jesus")
print(b)