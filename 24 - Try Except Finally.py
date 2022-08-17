try:
    result = 10 + 10
except:
    print("Hey it looks like you fucked up mate")
else:
    print("Well done!")
    print(result)


try:
    f = open('testfile','w')
    f.write("Write a test line")
except:
    print('All other exceptions!')
finally:
    print("Miłosz will always be sh*t")

def ask_for_init():

    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Huh, looks like it is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("Milosz loves Kulturka")

ask_for_init()