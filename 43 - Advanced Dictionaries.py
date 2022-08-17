#Advanced Dictionaries

d = {'k1':1,'k2':2}

print({x:x**2 for x in range(10)})

#If you would like to pass something different instead of number key values
print({k:v**2 for k,v in zip(['a','b'],range(2))})

for k in d.items():
    print(k)

