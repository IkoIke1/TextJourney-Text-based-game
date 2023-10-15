import random

life = 3
x = 0
coin = 10
Friend = 0
Friends = 0
Sword = 0

name = input('What is your name?:')
print("Hello, " + name + ".")

while x == 0:
    MonNum = random.randint(0,2)
    if MonNum == 0:
        #Frog
        MonLife = 2
        print("A frog appeared. What will you do?")
        while MonLife > 0:
            print("1:attack it. 2:Befriend it. 3:Run away.")
            move = input("What will you do?:")
            if move == "1":
                #Attack
                chance = random.randint(1,4)
                if chance == 1:
                    print("You miss.")
                    print("The frog's remaining health is ")
                    print(MonLife)
                else:
                    print("You hit the frog, dealing damage.")
                    MonLife = MonLife - (1 + Sword)
                    print("The frog's remaining health is ")
                    print(MonLife)
            else:
                if move == "2":
                    #Befriend
                    print("'Ribbit!', says frog. Nothing happened.")
                else:
                    #Run
                    chance = random.randint(1,5)
                    if chance == 1:
                       print("You got away!")
                       MonLife = 0
                    else:
                        print("You could not get away!")

            chance = random.randint(1,2)
            if chance == 1:
                print("You got attacked by a frog.")
                print("You lost 1 life.")
                life = life - 1
                print("Your remaining health is ")
                print(life)
            
    if MonNum == 1:
        #Doggo
        MonLife = 3
        print("A doggo appeared, what will you do?")
        while MonLife > 0:
            print("1:attack it. 2:Befriend it. 3:Run away.")
            move = input("Enter the number that you choose: ")
            if move == "1":
                #Attack
                chance = random.randint(1,4)
                if chance == 1:
                    print("You miss.")
                    print("The doggo's remaining health is ")
                    print(MonLife)
                else:
                    print("You hit the doggo, dealing damage.")
                    MonLife = MonLife - (1 + Sword)
                    print("The doggo's remaining health is ")
                    print(MonLife)
            else:
                if move == "2":
                    #Befriend
                    print("'Woof!', says doggo. He trusts you more now.")
                    Friend = Friend + 1
                    if Friend == 3:
                        MonLife = 0
                        Friends = Friends + 1
                        print("You have befriended the doggo!")
                else:
                    #Run
                    chance = random.randint(1,5)
                    if chance == 1:
                       print("You got away!")
                       MonLife = 0
                    else:
                        print("You could not get away!")
            chance = random.randint(1,2)
            if chance == 1:
                print("You got attacked by a doggo.")
                print("You lost 1 life.")
                life = life - 1
                print("Your remaining health is ")
                print(life)
                
    if MonNum == 2:
        #Cat
        MonLife = 9
        print("A cat appeared, what will you do?")
        while MonLife > 0:
            print("1:attack it. 2:Befriend it. 3:Run away.")
            move = input("Enter the number that you choose: ")
            if move == "1":
                #Attack
                chance = random.randint(1,4)
                if chance == 1:
                    print("You miss.")
                    print("The cat's remaining health is ")
                    print(MonLife)
                else:
                    print("You hit the cat, dealing damage.")
                    MonLife = MonLife - (1 + Sword)
                    print("The cat's remaining health is ")
                    print(MonLife)
            else:
                if move == "2":
                    #Befriend
                    print("'Meow!', says cat. He trusts you more now.")
                    if Friend == 4:
                        MonLife = 0
                        Friends = Friends + 1
                        print("You have befriended the cat!")
                else:
                    #Run
                    chance = random.randint(1,5)
                    if chance == 1:
                       print("You got away!")
                       MonLife = 0
                    else:
                        print("You could not get away!")
            chance = random.randint(1,2)
            if chance == 1:
                print("You got attacked by a cat.")
                print("You lost 1 life.")
                life = life - 1
                print("Your remaining health is ")
                print(life)

    if MonLife == 0:    
        #Coins
        chance = random.randint(1,10)
        coin = coin + chance
        print("Your amount of coins:")
        print(coin)
        
        chance = random.randint(1,10)
        if chance == 10:
            #Merchant
            print("You encountered a merchant.")
            if coin > 0:
                print("He offers you a sword for 10 coins.")
                print("1: Take the sword. 2: Refuse.")
                move = input("Enter the number that you choose: ")
                if move == "1" and coin > 10:
                    #Take sword
                    print("You take the sword.")
                    Sword = 1
                    coin = coin - 10
                    print("Your amount of coins:")
                    print(coin)
                else:
                    #Refuse
                    print("You refuse the sword.")