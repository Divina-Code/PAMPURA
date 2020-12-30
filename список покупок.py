a = False
while a != True:
    answer = int(input('press 1, 2 or 3 '))
    if answer == 1:
        add = input('choose what do you want to add ')
        productlist.append(add)
    elif answer == 2:
        dropout = int(input('choose number of what do you want to drop out '))
        productlist.pop(dropout)
    elif answer == 3:
        print(productlist)
    else:
        print('try again')
