import random 

def game():
    print("You are playing the game.")
    score = random.randint(1,100)
    with open("28.hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore= 0
    print(f"your score : {score}")
    if (score>hiscore):
        with open("28.hiscore.txt", "w") as f:
            f.write(str(score))

    return score 
game()
