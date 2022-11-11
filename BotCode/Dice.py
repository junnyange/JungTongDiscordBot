import random
    
def dice():
    myDice = random.randrange(1,7)
    botDice = random.randrange(1,7)
    if(myDice > botDice):
        return "승리", 0xFF0000, str(myDice), str(botDice)
    elif myDice < botDice:
        return "패배", 0xFAFA00, str(myDice), str(botDice)
    else:
        return "무승부", 0x00ff56, str(myDice), str(botDice)