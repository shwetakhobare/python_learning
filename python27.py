#prg to shuffle a deck of card

import itertools,random

deck = list(itertools.product(range(1,14),['Spad','Heart','Diamond','Club']))
random.shuffle(deck)

print("You got :")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])