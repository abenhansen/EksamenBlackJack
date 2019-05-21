from kort import Kort
from spiller import Hånd
import kort as k

deck = [] # Laver et array der skal indhole hele kort spillet
k.lavDeck(deck)  #Her laver vi kortene, giver dem farver og numre
helespillet = True
while helespillet:
    spiller1 = Hånd()
    dealer = Hånd()
    k.blandKort(deck) #Her blander vi kortene

    spiller1.tilføj_kort(k.delkort(deck))
    dealer.tilføj_kort(k.delkort(deck))
    spiller1.tilføj_kort(k.delkort(deck))
    dealer.tilføj_kort(k.delkort(deck))

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
    def playAgain():
        global helespillet
        while True:
            svar = input("Vil du spille igen? Tryk j eller n")
            if svar == "j":
                break
            elif svar == "n":
                helespillet = False
                break
            else:
                print("Du skal indtaste 'j' eller 'n'!")
                continue
    spiligang = True


    def træk_eller_stå():
        while True:
            global spiligang
            svar =input("Vil du trække et kort eller stå? Tryk 't' eller 's")
            if svar=="t":
                spiller1.tilføj_kort(k.delkort(deck))
                vis_hånd_spiller()
            elif svar=="s":
                print("Du har valgt at stå")
                while dealer.værdi<16:
                    dealer.tilføj_kort(k.delkort(deck))
                    vis_hånd_dealer()
                spiligang = False
                if dealer.værdi > 21:
                    print("Dealer har trukket over 21!")
                    print("Spiller har vundet!")
                    playAgain()
                elif spiller1.værdi>dealer.værdi:
                    print("Spiller har vundet!")
                    playAgain()
                elif dealer.værdi>spiller1.værdi:
                    print("Dealer har vundet!")
                    playAgain()
                elif dealer.værdi == spiller1.værdi:
                    print("Push! Det blev uafgjort!")
                    playAgain()
            else:
                print("Du skal indtaste 't' eller 's'!")
                continue
            break



    while spiligang:
        # vis_hånd_spiller()
        træk_eller_stå()
        if spiller1.værdi>21:
            print("Spiller har trukket over 21!")
            print("Dealer har vundet!")
            playAgain()
            break





# print("Du har valgt at stå")
#             if spiller1.værdi>dealer.værdi:
#                 print("Spiller har vundet!")
#             elif dealer.værdi>spiller1.værdi:
#                 print("Dealer har vundet!")
#             elif dealer.værdi == spiller1.værdi:
#                 print("Push! Det blev uafgjort!")






