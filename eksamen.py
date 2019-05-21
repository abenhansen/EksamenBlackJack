from kort import Kort
from spiller import Hånd
import kort as k

deck = [] # Laver et array der skal indhole hele kort spillet
k.lavDeck(deck)  #Her laver vi kortene, giver dem farver og numre

spiller1 = Hånd()
dealer = Hånd();
k.blandKort(deck) #Her blander vi kortene

spiller1.tilføj_kort(k.delkort(deck))
dealer.tilføj_kort(k.delkort(deck))
spiller1.tilføj_kort(k.delkort(deck))
dealer.tilføj_kort(k.delkort(deck))



def træk_eller_stå():
    spilIgang = None
    while True:
        svar =input("Vil du trække et kort eller stå? Tryk 't' eller 's")
        if svar=="t":
            spiller1.tilføj_kort(k.delkort(deck))
            for kort in spiller1.korthånd:
                print(kort)
        elif svar=="s":
            print("Du har valgt at stå")
            if spiller1.værdi>dealer.værdi:
                print("Spiller har vundet!")
            elif dealer.værdi>spiller1.værdi:
                print("Dealer har vundet!")
        else:
            print("Du skal indtaste 't' eller 's'!")
            continue
        break

def vis_hånd_spiller():
    print("Spillers hånd")
    for kort in spiller1.korthånd:
        print(kort)

def vis_hånd_dealer():
    print("Dealers hånd")
    for kort in dealer.korthånd:
        print(kort)
vis_hånd_spiller()
vis_hånd_dealer()
træk_eller_stå()







