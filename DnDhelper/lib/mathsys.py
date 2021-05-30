import random

# basic dice roll function
def diceRoll(numb):
    return random.randint(1, numb)

#combat function to determine suprise
def suprise(wis, dex):
    if(wis > dex):
        return "false"
    elif(wis == dex):
        chance = random.randint(0,1)
        if(chance == 1):
            return "false"
        else:
            return "true"
    else:
        return "true"

print(suprise(10,10))

