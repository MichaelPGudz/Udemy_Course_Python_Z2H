#First
st = 'Print only the words that start with s in this sentence'
str = st.split()
print(str)

for words in str:
    if words[0] == "s":
        print(words)

#Second - Range

print(list(range(0,11,2)))

#Third - List Comprehension
nums = [x for x in range(1,51) if x%3==0]
print(nums)

#Fourth - word count even
st = 'Print every word in this sentence that has an even number of letters'
str = st.split()

for i in str:
    if len(i)%2==0:
        print(f"even, those words are: {i}")

# Fifth - FizzBuzz
for i in range(1, 101):
    if i%3==0 and i%5==0:
        print(f"FizzBuzz! {i}")
    elif i%3==0:
        print("Fizz {}".format(i))
    elif i%5==0:
        print("Buzz {a}".format(a=i))
    else:
        print(f"regular {i}")

#Sixth - List Comprehension
st = 'Create a list of the first letters of every word in this string'
str = st.split()
print(str)
mylist = [x[0] for x in str]
print(mylist)
