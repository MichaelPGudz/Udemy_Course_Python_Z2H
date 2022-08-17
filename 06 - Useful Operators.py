#Range

for num in range(10):
    print(num)

#Range is a generator so you may want to cast it into list by
list(range(0,11,3))

#Enumarate

index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

index_count = 0
word = "Milosz smiec"
for letter in word:
    print(word[index_count])
    index_count +=1

for item in enumerate(word):
    print(item)
print("\n")
#Zip function
mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1,mylist2):
    print(item)
print(list(zip(mylist1,mylist2)))

#IN
print("mykey" in {"mykey": 345})
d = {"mykey":345}
print(345 in d.values())

#MIN and MAX

mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

#Random
from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]
print(shuffle(mylist))
print(mylist)

from random import randint
x =randint(0,100)
print(x)


