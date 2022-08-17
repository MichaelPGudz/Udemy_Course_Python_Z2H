#Advanced Lists
l = [1,2,3]
l.append(4)
print(l)

print(l.count(10))
print(l.count(1))

x = [1,2,3]
x.append([4,5])
print(x)

x = [1,2,3]
x.extend([4,5])
print(x)

print(l.index(2))

#Insertion
l.insert(2,'inserted before 3')
print(l)

#Poping off the elements
ele = l.pop(2)
print(l)

#Removing elements
l.remove(4)
print(l)

l = [1,2,3,4,3]
l.remove(3)
print(l)

#Reversing the list
l.reverse()
print(l)

#Sorting a list
l.sort()
print(l)