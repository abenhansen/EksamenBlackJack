import random
numre = ('to','tre','fire','fem','seks','syv','otte','ni','ti','bonde','dronning','konge','es')
farver =('hjerter','ruder','kløver','spade')

class Kort:

    def __init__(self,farve,nummer):
        self.farve = farve
        self.nummer = nummer



    def __str__(self):
        return self.farve + ": " + self.nummer


def lavDeck(deck):
    for farve in farver:
        for nummer in numre:
            deck.append(Kort(farve, nummer))

def blandKort(deck):
    random.shuffle(deck)
def delkort(deck):
        enkelt_kort = deck.pop()
        return enkelt_kort

