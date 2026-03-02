'''
rock = 1
paper= 2
scissors = 3
'''
import random

dict = {"rock" : 1,"paper" : 2, "scissors" : 3 }
friendstr = random.choice(["rock", "paper", "scissors"])
youstr = input("Enter your choice: ")
you = dict[youstr]
friend = dict[friendstr]
print(f"Friend chose: {friendstr}")

if (friend == you):
    print("Its Draw! play again.")


elif(friend ==2 and you == 3):
        print("You won!")
elif(friend ==1 and you == 3):
    print("Sad! You lose.")

elif(friend ==1 and you == 2):
    print("You won!")
elif(friend ==3 and you == 2):
    print("Sad! You lose.")

elif(friend ==3 and you == 1):
    print("You won!")

elif(friend ==3 and you == 2):
    print("Sad! You lose.")
elif(friend ==2 and you == 1):
    print("Sad! You lose.")


elif(friend ==1 and you == 3):
    print("Sad! You lose.")


