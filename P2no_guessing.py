import random
print("Hey welcome to the game")
score=0

while True:
    player=int(input("enter a number b/w 0 to 5 : "))
    if player > 5 or player < 0:
        print ("choose a number b/w 0 to 5 only")
    else:
        comp=random.randrange(0,6)
        print("Number gussed by computer is:",comp)

        if player == comp :
            print("you won!!! ")
            score += 1
            a=input("Do you want to continue the game ??(yes/no)")
            if a.lower() != "yes" :
                break 
        
        else:
            print("you lost :(")

print("your score is :" , +score)
print("THANK YOU :)")

