def square(num):

    return num**2
my_nums = [1,2,3,4,5]

map(square,my_nums)

for item in map(square,my_nums):
    print(item)

list(map(square,my_nums))

def slicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

print(list(map(slicer, names)))

def check_even(num):
    return num%2==0

mynums = [1,2,3,4,5,6]

filter(check_even, mynums)
for n in filter(check_even, mynums):
    print(n)

# Function to be modified into lambda expression
def suqare(num):
    result = num ** 2
    return result

something = lambda num: num ** 2
print(something(3))
#Map and Lambda Combination
print(list(map(lambda num:num**2, mynums)))
#Filter Lambda combination
print(list(filter(lambda num:num%2 == 0, mynums)))
#Map lambda first letter combination
print(list(map(lambda x:x[0],names)))
