x = 50

def printer():
    x = 50
    return x

print(x)

def func(x):
    print(f'X is {x}')

    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    return x

x = func(x)
print(x)