import random
print("Welcome to Zoo Camel!")
print("You have stolen a camel from the zoo, and you are trying to get home.")
print("The zookeeps want their camel back and are chasing you down! Survive your")
print("adventure home and out run the zookeepers.")
print()

done = False
milesTraveled = 0
nativesTraveled = -20
camelTiredness = 0
thirst = 0
canteen = 3
oasis = -1

while not done :
        
   
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print()
    
    userInput = input("What will you do? ")
    
    if userInput.upper() == "Q" :
        done = True
  
    elif userInput.upper() == "E" :
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteen)
        print("The natives are", milesTraveled - nativesTraveled, "miles behind you.")
        print()
    
    elif userInput.upper() == "D" :
        print("You took a break.")
        print("Your camel is happy.")
        print("The zoo keepers did not give up.")
        print()
        camelTiredness = 0
        nativesTraveled += random.randrange(7, 15)
    
    elif userInput.upper() == "C" :
        miles = random.randrange(10, 21)
        milesTraveled += miles
        thirst += 1
        camelTiredness += random.randrange(1, 4)
        nativesTraveled += random.randrange(7, 15)
        oasis = random.randrange(20)
        if oasis == 10 :
            thirst = 0
            camelTiredness = 0
            canteen = 3
            print("You found some water")
            print("You start to drink water , and")
            print("Your camel is resting!")
            print("The zoo keepers continue the chase.")
            print()
        else :
            print("You push onward at full speed, moving a total of", miles, "miles")
            print("Your thirst increases.")
            print("The zookeepers continue the run.")
            print()
   
    elif userInput.upper() == "B" :
        miles = random.randrange(5, 13)
        milesTraveled += miles
        thirst += 1
        camelTiredness += 1
        nativesTraveled += random.randrange(7, 15)
        oasis = random.randrange(20)
        if oasis == 10 :
            thirst = 0
            camelTiredness = 0
            canteen = 3
            print("You found some water")
            print("You start to drink water , and")
            print("Your camel is rested!")
            print("The zoo keeprs continue the chase.")
            print()
        else :
            print("You move forward, moving a total of", miles, "miles")
            print("Your thirst increases.")
            print("The zoo keepers continue the chase.")
            print()
   
    elif userInput.upper() == "A" :
        if canteen > 0 :
            canteen -= 1
            thirst = 0
            print("You take a drink")
        else:
            print("Your canteen is empty. You imagine yourself as dead meat.")
    
  
    if thirst > 5 :
        print("You died of thirst!")
        print("Game Over.")
        print()
        done = True
    elif thirst > 4 :
        print("You are thirsty!")
    
    if milesTraveled >= 200 :
        print("Congratulations! You have escaped!")
        print("You win!")
        print()
        done = True
  
    if camelTiredness > 8 :
        print("Your camel died of exhaustion!")
        print("With no camel, the zoo keepers catch up to you and arrest you")
        print("on the spot.")
        print("Game Over.")
        print()
        done = True
    elif camelTiredness > 5 :
        print("Your camel is tired.")
        print()
    
    if milesTraveled - nativesTraveled <= 0 :
        print("The zoo keepers have caught up with you!")
        print("They catch up to you and arrest you, and take their camel back.")
        print("Game Over.")
        print()
        done = True
    elif milesTraveled - nativesTraveled < 15 :
        print("You see faint shapes on the horizon behind you.")
        print("The zoo keepers are getting close!")
        print()

print(" Goodbye.")
input("")
