import random as rn
from time import sleep

p1 = []
p2 = []
house = []
suits = ["hearts", "spades", "clubs", "diamonds"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

#Retrieves the sum of a given list of card tuples
def sum(hand):
    sum = 0
    num_aces = 0
    for i, j in hand:
        if i == 'J' or i == 'Q' or i == 'K':
            sum += 10
        elif i == 'A':
            num_aces += 1
        else:
            sum += i
    for i in range(num_aces):
        if sum + 11 <= 21:
            sum += 11
        else:
            sum += 1
    return sum

def bust(hand):
    return sum(hand) > 21

# Checks the various conditions by which the game could end.
def gameOver():
    if bust(p1) or bust(house) or sum(house) == 21 or sum(p1) == 21:
        return True
    return False

# The main gameplay loop for a game against the house
def singleGame():
    deck = []
    move = 0
    for i in values:
        for j in suits:
            deck.append([i, j])
    rn.shuffle(deck)
    p1.append(deck[0])
    p1.append(deck[1])  
    house.append(deck[2])
    house.append(deck[3])
    curr = 4
    print(f"The Dealer shows {house[1:]}")
    print(f"Your current hand is: {p1}")
    if sum(p1) == 21:
        print("Your total is 21! You got BlackJack, you win!")
        return
    print(f"Your current total is: {sum(p1)}")

    #core gameplay loop of hit/stand
    while(1):
        i = int(input("\nDo you Hit (Press 1) or Stay (Press 0): "))
        if i==1 or i==0:
            move = i
        else:
            print("Enter a valid number....\n")
        
        if move == 1:
            p1.append(deck[curr])
            print(f"\nYou draw: {deck[curr]}") 
            print(f"Your current hand is: {p1}")
            if bust(p1):
                print("You busted! Sorry, but the house always wins.")
                return
            print(f"You're at {sum(p1)}")
            curr += 1
            continue

        if move == 0:
            print(f"\nThe house's second card was {house[0]}")
            while sum(house) < 17:
                sleep(1)
                house.append(deck[curr])
                print(f"The house draws: {deck[curr]}") 
                print(f"The house's current hand is: {house}")
                if bust(house):
                    print("The house busted! You win!")
                    return
                print(f"The house is at {sum(house)}")
                curr += 1
        
        #sleep added for better gameplay flow
        sleep(.5)
        #checking various win conditions to print proper end-of-game message
        if sum(p1) > sum(house):
            print(f"Your total is {sum(p1)}, which is higher. You win!")
            break
        elif sum(house) > sum(p1):
            print(f"The house's total is {sum(house)}, which is higher than yours. You lose.")
            break
        elif sum(house) == sum(p1):
            print(f"You tied the house at {sum(p1)}The house wins ties! Sorry, you lose.")
            break
    return

def main():
    print("Welcome to BlackJack!")
    playAgain = 1
    while(playAgain == 1):
        global p1, p2, house
        p1, p2, house = [], [], []
        while(1):
            i = int(input("\nPress 1 to play!"))
            if i==1:
                singleGame()
                break
            else:
                print("Enter a valid number....\n")
        # Gives a play again option after the game ends
        while(1):
            i = int(input("\nPress 1 to play again, or press 0 quit: "))
            if i==1 or i==0:
                playAgain = i
                break
            else:
                print("Enter a valid number....\n")

if __name__ == '__main__':
    main()
