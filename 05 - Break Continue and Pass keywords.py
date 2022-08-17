#Pass
x = [1,2,3]

for i in x:
    pass
print("You did it! It passed!")

#Continue
mystring = "Sammy"
for letter in mystring:
    if letter == "a":
        continue
    print(letter)

#Break
print("\n")
mystring = "Sammy"
for letter in mystring:
    if letter == "a":
        break
    print(letter)

y = 0
while y < 5 :
    if y ==2:
        break
    print(y)
    y +=1