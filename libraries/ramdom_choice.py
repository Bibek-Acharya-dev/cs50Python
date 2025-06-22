import random 
import math


coin=random.choice(["heads","tails"])
print(coin)

# random integer
value=random.randint(1,10)
print(value)


# random float
floatvalue=round(random.uniform(1.1,5.0),2)
print(floatvalue)

if floatvalue%int(floatvalue)>0.5:
    print(math.ceil(floatvalue))
else:
    print(math.floor(floatvalue))    


cards=["jack", "king", "queen"]
random.shuffle(cards)

for card in  cards:
    print(card)