try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("The elements in the list are not a numbers!")
try:
    x = 5
    y = 0
    z = x/y
except:
    print(f"Cannot divide by {y}!")
finally:
    print("All Done!")



def ask():

    while True:
        try:
            number = int(input("Please provide a number: "))
        except:
            print("Huh, seems that is not a number. Please try again.\n")
            continue
        else:
            print(f"Got it! The square of the number you entered is {number**2}.")
            break
ask()