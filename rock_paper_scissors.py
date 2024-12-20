import random

def prompt(message):
    print(f"=> {message}")

def rock_paper_scissors():
    VALID_CHOICE = ["rock", "paper","scissors"]
    prompt("Please pick from these: Rock || Paper || Scissors")
    your_choice = input().lower()
    
    while your_choice not in VALID_CHOICE:
        prompt("Invalid choice. Please pick again.")
        your_choice = input()
    
    match your_choice:
        case 'rock': prompt("You picked the rock")
        case 'paper': prompt("You picked the paper")
        case 'scissors': prompt("You pick the scissors")
    
    computer_choice = random.choice(VALID_CHOICE).lower()
    
    if your_choice == 'rock' and computer_choice == 'rock':
        prompt("Computer also picked Rock. It is tie game") 
        return 1
    if your_choice == 'rock' and computer_choice == 'paper':
        prompt("Computer picked Paper. You lose!!!")
        return 0
    if your_choice == 'rock' and computer_choice == 'scissors':
        prompt("Computer picked Scissors. Congratulation!! You win!")
        return 2
    if your_choice == 'paper' and computer_choice == 'rock':
        prompt("Computer picked Rock. Congratulation!! You win!!") 
        return 2
    if your_choice == 'paper' and computer_choice == 'paper':
        prompt("Computer also picked Paper. It is a tie game!")
        return 1
    if your_choice == 'paper' and computer_choice == 'scissors':
        prompt("Computer picked Scissors. You lose!")
        return 0   
    if your_choice == 'scissors' and computer_choice == 'rock':
        prompt("Computer picked Rock. You lose!") 
        return 0
    if your_choice == 'scissors' and computer_choice == 'paper':
        prompt("Computer picked Paper. Congratulation!! You win")
        return 2
    if your_choice == 'scissors' and computer_choice == 'scissors':
        prompt("Computer also picked Scissors. It is a tie game!")
        return 1 

your_point = 0
computer_point = 0 
    
while your_point < 3 and computer_point < 3:
    result = rock_paper_scissors()
    if result == 0:
        computer_point += 1
        print(f"Score now {your_point}-{computer_point}")
    if result == 2:
        your_point += 1
        print(f"Score now {your_point}-{computer_point}")
    if result == 1:
        print(f"Score now {your_point}-{computer_point}")
if your_point == 3:
    print(f"You win with the score {your_point}-{computer_point}")
if computer_point == 3:
    print(f"You lose with the score {your_point}-{computer_point}")
