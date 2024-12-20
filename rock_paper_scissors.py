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
    if your_choice == 'rock':
        match computer_choice:
            case 'rock': prompt("Computer also picked Rock. It is tie game")
            case 'paper': prompt("Computer picked Paper. You lose!!!")
            case 'scissors': prompt("Computer picked Scissors. Congratulation!! You win!")
    if your_choice == 'paper':
        match computer_choice:
            case 'rock': prompt("Computer picked Rock. Congratulation!! You win")
            case 'paper': prompt("Computer also picked paper. It is a tie game")
            case 'scissors': prompt("Computer picked Scissors. You lose")
    elif your_choice == 'scissors':
        match computer_choice:
            case 'rock': prompt("Computer picked Rock. You lose")
            case 'paper': prompt("Computer picked Paper. Congratulation!! You win!")
            case 'scissors': prompt("Computer also picked Scissors. It is a tie game!")
play_again = 'y'
while play_again == 'y':
    rock_paper_scissors()
    prompt("Do you want to play again: y/n")  
    play_again = input() 