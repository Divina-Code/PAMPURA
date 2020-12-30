print("Hello user")
from random import shuffle
letters = list("qwerrtyuiopasdfghjklzxcvbnm")
numbers = list("1234567890")
symbols = list("!@#$%^&*")
capital = list("QWERTYUIOPASDFGHJKLZXCVBNM")
list =(symbols + numbers + capital + letters)
shuffle(list)
print(''.join(list[0:8]))
