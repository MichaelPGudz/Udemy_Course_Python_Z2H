def func() :
    return 1

func()

def hello():
    return "Hello!"

hello()

greet = hello

greet()

del hello

greet()

def hello(name='Mike'):
    print('The hello function has been excuted!')

    def greet():
        return '\t This is the greet() function inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())
    print(welcome())
    print('This is the end of the hello function!')

hello()
print("\n")

def hello(name='Mike'):
    print('The hello function has been excuted!')

    def greet():
        return '\t This is the greet() function inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print("I am going to return a function!")

    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello('Jose')

my_new_func()

def cool():

    def super_cool():
        return 'I am super cool!'

    return super_cool

some_func = cool()
some_func()

def hello():
    return 'Hi Mike!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello)

print("\n Wow Big shot!")

def new_decorator(original_func):

    def wrap_func():

        print('Some extra code before the original function execution')

        original_func()

        print('Some extra code, after the original function!')

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

print("\nHere it comes")

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()