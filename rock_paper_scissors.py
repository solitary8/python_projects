import random
import time

rock_paper_scissors = ("rock" , "paper" , "scissors")
replay = "y"
computer_score = 0
player_score = 0
while replay == "y":
    computer_choice = random.choice(rock_paper_scissors)
    player_choice = input("rock paper or scissors ? : ")

    print("Rock")
    time.sleep(0.5)
    print("Paper") 
    time.sleep(0.5)
    print("Scissors")
    time.sleep(0.5)
    if(computer_choice == "rock"):
        if(player_choice == "rock"):
            print("It's a tie !")

        elif(player_choice == "paper"):
            print("Player wins ! ")

        elif(player_choice == "scissors"):
            print("Computer wins !")

    elif(computer_choice == "paper"):
        if(player_choice == "rock"):
            print("Computer wins ! ")

        elif(player_choice ==  "paper"):
            print("It's a tie !")

        elif(player_choice == "scissors"):
            print("Player wins ! ")
    elif(computer_choice == "scissors"):
        if(player_choice == "rock"):
            print("Player wins !")
            player_score += 1
        
        elif(player_choice == "paper"):
            print("Computer wins !")
            computer_score += 1
        
        elif(player_choice == "scissors"):
            print("It's a tie !")
    print("Computer's score is : ",computer_score, "Player's score is : ",player_score)
    replay = input("Replay ?(y/n): ")
    