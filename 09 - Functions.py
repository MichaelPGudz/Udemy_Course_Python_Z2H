name = "Miga"

def say_hello(name="NAME"):
    print("Hello " +name)

say_hello()

name = "Miga"

def say_hello(name):
    print(0 + name)

say_hello(123)

#Find out if the word "dog" is in a string?

def dog_check(s):
    return "dog" in s.lower()

ss = dog_check("Wuf wuf Dog")
print(ss)

#Pig Latin
def pig_latin(word):
    vowels = ['a','e','i','o','u','y']
    if word[0] in vowels:
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

pig = pig_latin('word')
print(pig)

#Jose resolution

def pig_latin(word):

    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

res = pig_latin("word")
print(res)