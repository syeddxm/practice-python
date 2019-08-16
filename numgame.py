#generate a random number between 1-10
#get an umber from a player
#comare guess to number
#peint hit or miss

import random
target = random.randint(1,100)

while True:
    player = input("What's your guess? ")
    if player > target:
        print("high")
    elif player < target:
        print("low")
    else:
        print("hit")
        break
