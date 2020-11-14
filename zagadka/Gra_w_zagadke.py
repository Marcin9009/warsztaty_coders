from random import randint
print("Guess the number from the range")
comp = randint(1,100)
user = -1
i = 0
while user != comp:
    i += 1
    try:
        user = int(input("Guess the number: "))
    except ValueError:
        print("it' not a number!")
        continue
    if user < comp:
        print("TO samll!")
    elif user > comp:
        print("To big!")
    else:
        print("You winn!")
        break