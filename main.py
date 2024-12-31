import random

# Generate a random number from -1, 0, 1
computer = random.choice([-1, 0, 1])

youstr=input("Enter your choice:")
youdict={"s":1,"w":-1,"g":0}
# reversedict={1:"snake",-1:"water",0:"gun"}

you=youdict[youstr]
if(computer==you):
    print("it's draw")   
elif(computer==-1 and you==1):
    print("you win!")
elif(computer==-1 and you==0):
    print("you lose!")
elif(computer==1 and you==-1):
    print("you lose!")
elif(computer==1 and you==0):
    print("you win!")
elif(computer==0 and you==1):
    print("you lose!")
elif(computer==0 and you==-1):
    print("you win!")
else:
    print("Somthing went wrong")    

