mystring = "hello"
print(list(mystring))

mylist = []
for letter in mystring :
    mylist.append(letter)

print(mylist)

#List comprehension

mylist = [letter for letter in mystring]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

mylist = [x for x in range(0,11) if x%2==0]
print(mylist)

celcius = [0,10,20,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

#Listen Comprehension broken down

fahrenheit = []
for temp in celcius:
    fahrenheit.append((9/5)*temp + 32)

print(fahrenheit)

#If and else in list comprehension

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

#Nested loop
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)

#Nested loop in list comprehension

mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
print(mylist)
