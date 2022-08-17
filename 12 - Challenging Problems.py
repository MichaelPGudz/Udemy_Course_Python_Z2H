def spy_game(nums):

    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code)== 1

# Check
x = spy_game([1,2,4,0,0,7,5])
print(x)

# Check
x = spy_game([1,0,2,4,0,5,7])
print(x)

# Check
x = spy_game([1,7,2,0,4,5,0])
print(x)

def count_primes(num):

    #Check for 0 or 1
    if num <2:
        return 0

    # 2 or greater
    primes = [2]
    x = 3

    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x +=2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)



# Check
x = count_primes(100)
print(x)

print("\n")

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('a')
