from random import randint

def rps(your_choice):
    computer= randint(1,3)
    print("computer choice:",computer)
    if your_choice == computer:
        return "draw"
    else:
        if your_choice == 1 and computer == 2:
            return "lose"
        elif your_choice == 1 and computer == 3:
            return "win"
        elif your_choice == 2 and computer == 1:
            return "win"
        elif your_choice == 2 and computer == 3:
            return "lose"
        elif your_choice == 3 and computer == 1:
            return "lose"
        elif your_choice == 3 and computer == 2:
            return "win"
        else:
            pass

if __name__ == "__main__":
    quit=False
    round=0
    while quit == False:
        print("welcome to Rock(1) Paper(2) Scissors(3) Game!")
        your_choice=int(input())
        print(rps(your_choice))
        print("still wanna play? Y/N")
        answers=input()
        if answers == "N" or answers == "n":
            quit = True 
        else:
            round+=1
            print("round",round)

