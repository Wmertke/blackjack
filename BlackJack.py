import random

cardArray = [2 ,3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
cardValues = [2 ,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
name = input("Welcome to Black Jack Lucky Duck Casino, what's your name, my guy? ")
playResponse = input("Hi " + name + ", Do you want to play Black Jack? [y/n] ")
if playResponse == "n":
    print("Ok " + name + ", see you around later I guess.  Why even run this program if you want to say no?")
    exit(1)
ruleResponse = input ("Cool beans, let me set up the table for us. Do you already know the house rules?  [y/n] ")
if ruleResponse == "n":
    print("Get as close to 21 as you can without going over.\nNumber cards are equal to their respective values while face cards have a value of 10.")
    print("Aces have a value of 11, but if you are over 21 their value can change to 1, giving you another chance.")
    print("You auto win if you hit 21 on the initial draw, but the dealer wins all ties.")
    print("Whoever is closest to 21 without going over wins the bet.\nThe game ends when you run out of money.\n'hit' gives you another card while 'stay' ends your turn.")
gameResponse = input("Would you like to start a round of Black Jack? [y/n] ")
if gameResponse == "n":
    print("Ok, see you later")
    exit(1)
cashAmount = int(input("How much money would you like to start with? [numeric value] $"))
startingAmount = cashAmount
peakAmount = startingAmount
while (cashAmount > 0):
    cardsInHand = []
    dealersHand = []
    betAmount = int(input("How much coin would you like to wager? $"))
    while (betAmount > cashAmount):
        print ("Dishonnesty only works for the house, please enter a valid bet size")
        betAmount = int(input("$"))
    hasBusted = False
    hasConceeded = False
    cardValue = 0
    dealerValue = 0
    firstCard = random.randint(0,12)
    secondCard = random.randint(0,12)
    dealerFirst = random.randint(0,12)
    dealerSecond = random.randint(0,12)
    cardsInHand.append(firstCard)
    cardsInHand.append(secondCard)
    dealersHand.append(dealerFirst)
    dealersHand.append(dealerSecond)
    cardValue = cardValues[firstCard] + cardValues[secondCard]
    dealerValue = cardValues[dealerFirst] + cardValues[dealerSecond]
    print ("Your first card is: " + str(cardArray[firstCard]))
    print ("The dealer's first card is: " + str(cardArray[dealerFirst]))
    print ("Your second card is: " + str(cardArray[secondCard]))
    print ("The dealer's second card is hidden.")
    if cardValue == 21:
        cashAmount += betAmount
        if peakAmount < cashAmount:
            peakAmount = cashAmount
        print("You won. You now have $" + str(cashAmount) + ".")
        hasBusted = True
    while cardValue <= 21 and hasBusted == False:
        choice = input("Currently, you have a value of " + str(cardValue) + ".  Do you want to 'hit' or 'stay'? ")
        if choice == "hit":
            newCardValue = random.randint(0,12)
            cardsInHand.append(cardArray[newCardValue])
            cardValue += cardValues[newCardValue]
            print("You drew a "+ str(cardArray[newCardValue]) + " giving you a total of " + str(cardValue))
            if cardValue == 21:
                cashAmount += betAmount
                if peakAmount < cashAmount:
                    peakAmount = cashAmount
                print("You won. You now have $" + str(cashAmount) + ".")
                hasBusted = True
            if cardValue > 21:
                if "A" in cardsInHand:
                    cardValue -= 10
                    print("Your Ace value has changed from an 11 to a 1. Your new value is " + str(cardValue) + ".")
                    cardsInHand.remove("A")
                else:
                    cashAmount -= betAmount
                    print("You busted and lost your money. You now have $" + str(cashAmount) + ".")
                    hasBusted = True
        if choice == "stay":
            hasBusted = True
            if dealerValue > 21:
                cashAmount += betAmount
                if peakAmount < cashAmount:
                    peakAmount = cashAmount
                print("The dealer busted. You now have $" + str(cashAmount) + ".")
                hasConceeded == True
            print("The dealers hidden card was "+ str(cardArray[dealerSecond]) + " giving him a value of " + str(dealerValue))
            if dealerValue > cardValue and dealerValue <= 21:
                    cashAmount -= betAmount
                    print("The dealer won. You now have $" + str(cashAmount) + ".")
                    hasConceeded == True
            if dealerValue == cardValue:
                cashAmount -= betAmount
                print("The dealer won. You now have $" + str(cashAmount) + ".")
                hasConceeded == True
            while dealerValue < cardValue and cardValue <= 21 and hasConceeded == False:
                newDealerCard = random.randint(0,12)
                dealersHand.append(cardArray[newDealerCard])
                dealerValue += cardValues[newDealerCard]
                print("The dealer drew a "+ str(cardArray[newDealerCard]) + " giving him a total of " + str(dealerValue))
                if dealerValue == cardValue:
                    cashAmount -= betAmount
                    print("The dealer won. You now have $" + str(cashAmount) + ".")
                    hasConceeded == True
                if dealerValue > cardValue and dealerValue <= 21:
                    cashAmount -= betAmount
                    print("The dealer won. You now have $" + str(cashAmount) + ".")
                    hasConceeded == True
                if dealerValue > 21:
                    if "A" in dealersHand:
                        dealerValue -= 10
                        print("The dealer's Ace value has changed from an 11 to a 1. His new value is " + str(dealerValue) + ".")
                        dealersHand.remove("A")
                    else:
                        cashAmount += betAmount
                        if peakAmount < cashAmount:
                            peakAmount = cashAmount
                        print("The dealer busted. You now have $" + str(cashAmount) + ".")
                        hasConceeded == True
print ("Thanks for playing " + name + ". You started out with $" + str(startingAmount) + " and peaked at $" + str(peakAmount) + ".")
print ("Please come back to Black Jack Lucky Duck anytime you're bored.")