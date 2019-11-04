import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit() == True:
    number = int(sys.argv[1])
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
elif len(sys.argv) > 1:
    print("ERROR")
else:
    pass
