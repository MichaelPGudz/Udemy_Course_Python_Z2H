def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        if a > b:
            return a
        else:
            return b

# Check
x = lesser_of_two_evens(2,4)
print(x)
# Check
x = lesser_of_two_evens(2,5)

print(x)

def animal_crackers(text):
    a = text.split()
    if a[0][0] == a[1][0]:
        return True
    else:
        return False


# Check
x = animal_crackers('Levelheaded Llama')
print(x)
# Check
x = animal_crackers('Crazy Kangaroo')
print(x)

def makes_twenty(n1,n2):
    if n1==20 or n2==20 :
        return True
    else:
        if n1+n2 ==20:
            return True
        else:
            return False

# Check
x = makes_twenty(20,10)
print(x)
# Check
x = makes_twenty(2,3)
print(x)

def old_macdonald(name):
    spt = name[:3].capitalize()
    spt2 = name[3:].capitalize()
    return spt+spt2

# Check
x = old_macdonald('macdonald')
print(x)

def master_yoda(text):
    x = text.split()
    x.reverse()
    x = " ".join(x)
    return x


# Check
x = master_yoda('I am home')
print(x)
# Check
y = master_yoda('We are ready')
print(y)

def almost_there(n):

    return abs(100-n) <= 10 or abs(200-n) <=10

# Check
x = almost_there(104)
print(x)

# Check
x = almost_there(150)
print(x)

# Check
x = almost_there(209)
print(x)

print("\n")

def has_33(nums):

    for i in range(0,len(nums)-1):
       if nums[i] == 3 and nums[i+1] == 3:
           return True

    return False


# Check
x = has_33([1, 3, 3])
print(x)

# Check
y= has_33([2, 3, 1, 3])
print(y)

# Check
z = has_33([3, 1, 3])
print(z)

def paper_doll(text):
    result= ""
    for i in text:
        result+=i*3
    return result

x = paper_doll('Hello')
print(x)

# Check
x = paper_doll('Mississippi')
print(x)

def blackjack(a,b,c):
    sum = a+b+c

    if sum <= 21:
        return sum
    elif sum > 21 and 11 in [a,b,c]:
        return sum-10
    else:
        return "BUST"



# Check
x = blackjack(5,6,7)
print(x)

# Check
x = blackjack(9,9,9)
print(x)

# Check
x = blackjack(9,9,11)
print(x)

print("\n")

def summer_69(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] in [6,7,8,9]:
           pass
        elif arr[i] in []:
            return 0
        else:
            sum += arr[i]
    return sum

# Check
x = summer_69([1, 3, 5])
print(x)

# Check
x = summer_69([4, 5, 6, 7, 8, 9])
print(x)

# Check
x = summer_69([2, 1, 6, 9, 11])
print(x)

x = summer_69([])
print(x)
