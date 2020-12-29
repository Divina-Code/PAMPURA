print("hello,players")
import random
from time import sleep
player1 = random.randint(1, 11)
player2 = random.randint(1, 11)

inGame1 = True
inGame2 = True
while inGame1 and inGame2:
    if inGame1 and inGame2:
        take_card = str((input("Player1 , would you like to take card Yes/No")))
        if take_card == "Yes":
            card1 = random.randint(1, 11)
            print("card =", card1)
            player1 = player1 + card1
            print(player1 , ",now you got points", player1)
        elif take_card == "No":
            inGame1 = False
        else :
            print("I do not understand you")
        take_card = str((input("Player2 , would you like to take a card Yes/No")))
        if take_card == "Yes":
            card2 = random.randint(1, 11)
            print("card =", card2)
            player2 = player2 + card2
            print(player2, ",now you got points", player2)
        elif take_card == "No":
            inGame2 = False
if player1 == 21:
    print("Good job")
elif player1 > player2:
    print(player1, "you win")
elif player1 > 21:
    print(player1, "you win")
else:
    print(player1,"you lose")









