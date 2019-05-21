from kort import Kort
from spiller import Hånd
import kort as k

deck = [] # Laver et array der skal indhole hele kort spillet
k.lavDeck(deck)  #Her laver vi kortene, giver dem farver og numre
k.blandKort(deck)
penge=100
number_of_hands=0
helespillet = True
while helespillet:
    # print(len(deck))
    print("Du har så mange penge: {0}".format(penge))
    bet = 0
    spiller1 = Hånd()
    dealer = Hånd()
    if number_of_hands==4:
        deck.clear()
        k.lavDeck(deck)
        k.blandKort(deck) #Her blander vi kortene
    number_of_hands += 1
    def betting():
        while True:
            try:
                svar = int(input("Hvor meget vil du bette? Tast 0 hvis du bare vil spille for sjov"))
                if svar>penge:
                    print("Du har ikke nok penge!")
                    continue
            except ValueError:
                print("Ikke et tal! Prøv igen!.")
                continue
            else:
                return svar
                break
    bet = betting()
    penge=penge-bet
    print(bet)
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
            global penge
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
                    penge = penge+(bet*2)
                    playAgain()
                elif spiller1.værdi>dealer.værdi:
                    print("Spiller har vundet!")
                    penge = penge+(bet*2)
                    playAgain()
                elif dealer.værdi>spiller1.værdi:
                    print("Dealer har vundet!")
                    playAgain()
                elif dealer.værdi == spiller1.værdi:
                    print("Push! Det blev uafgjort!")
                    penge=penge+bet
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






