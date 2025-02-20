print("Hey welcome to the game")

play= input("do you want to play the game (yes/no)")
if play.lower() != "yes":
    quit()


print("lets play the game!!")
score = 0

q=input("what is full form of FTP ?")
if q.lower() == "file transfer protocol" :
    print("correct")
    score += 1

else:
    print("incorrect!")

q=input("what is full form of PNG ?")
if q.lower() == "portable network graphics" :
    print("correct")
    score += 1

else:
    print("incorrect!")

q=input("what is full form of CPU ?")
if q.lower() == "central processing unit" :
    print("correct")
    score += 1

else:
    print("incorrect!")

q=input("which key works as an eraser ?")
if q.lower() == "backspace key" or "backspace" :
    print("correct")
    score += 1

else:
    print("incorrect!")

q=input("full form of OOPS ?")
if q.lower() == "object oriented programming system" :
    print("correct")
    score += 1

else:
    print("incorrect!")

print("you got" +str(score) +"questions correct")
print("you got" +str((score/5)*100) +"%")