
isGuessed = False

while isGuessed != True :
    task = "Choose the number between 1 and 10 "

    answer = input(task)

    if answer == "6":
        print("Yes ,it is right")
        isGuessed = True
    elif answer == "7":
        print("It is not right.Try again.")
    else :
        print("What a pity((Try again")

print("GGWP")
