import random 
#Guessing Number Program
n = random.randint(1,100)
def gradient():
    X = int(input("Enter the number "))
    if(X==n):
        print("Game Over")
    elif(X<n):
        print("Your number is smaller than expected")
        gradient()
    elif(X>n):
         print("Your number is greater than expected")
         gradient()

gradient()
    