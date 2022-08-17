#Advanced sets methods

s = set()
s.add(1)
s.add(2)
s
s.clear()

s = {1,2,3}
sc = s.copy()
s.add(4)

s.difference(sc)

#Set difference update method
s1 = {1,2,3}
s2 = {1,4,5}

s1.difference_update(s2)

print(s1)

s.discard(2)

s1 = {1,2,3}
s2 = {1,2,4}

s1.intersection(s2)

s1.intersection_update(s2)

print(s1)

#
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

s1.isdisjoint(s2)
s1.isdisjoint(s3)

#If one set is another one's subset
s1.issubset(s2)

#If one set is another one's extension

s2.issuperset(s1)

#Symmetric difference
s1.symmetric_difference(s2)

#Union of two sets
s1.union(s2)

s1.update(s2)