
isGuessed = False

while isGuessed != True:
    task = "25* 8.."

    answer = input(task)

    if answer == "200":
        print("красавчик")
        isGuessed = True
    elif answer == "400":
        print("неудачно , попробуй еще раз)")
    else:
        print("Не совсем")

print("Спасибо за игру")
