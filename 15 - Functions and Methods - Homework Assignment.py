def vol(rad):
    return 4/3*3.14*rad**3

# Check
x = vol(2)
print(x)

def ran_check(num,low,high):
    spectrum = list(range(low,high+1))
    if num in spectrum:
        return f'{num} is in the range beetween {low} and {high}'
    else:
        return f"{num} is not in the range beetween {low} and {high}"

# Check
x = ran_check(5,2,7)
print(x)

def ran_bool(num,low,high):
    spectrum = list(range(low, high + 1))
    return num in spectrum

#Check
x = ran_bool(3,1,10)
print(x)

def up_low(str):
    lowcount = 0
    upcount = 0
    for letter in str:
        if letter.islower():
            lowcount +=1
        elif letter.isupper():
            upcount +=1
    return f'No. of Upper case characters: {upcount}\nNo. of Lower case characters:{lowcount}'

str = 'Hello Mr. Rogers, how are you this fine Tuesday?'
x = up_low(str)
print(x)

def unique_list(lst):
    new_lst = list(set(lst))
    return new_lst

x = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(x)

def multiply(numbers):
    result = 1
    for nums in numbers:
        result *= nums
    return result

x = multiply([1,2,3,-4])
print(x)

def palindrome(s):
    return s == s[::-1]

x = palindrome('helleh')
print(x)

print("\n")
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str = set(str1.lower())
    alpha = set(alphabet)
    str.discard(" ")
    return str == alpha


x = ispangram("The quick brown fox jumps over the lazy dog")
print(x)
