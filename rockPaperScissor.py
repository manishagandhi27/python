# Rock paper scissors game
# Rock smashes scissors
# Paper cover  rock
# scissor cuts paper

import random

while True:
    user_choice = input("Your Choice? (Rock, Paper, Scissor) ")
    possible_inputs = ['Rock', 'Paper', 'Scissor']
    system_choice = random.choice(possible_inputs)

    print(f"\n User choice is {user_choice} and system choice is {system_choice}")

    # Rules
    if user_choice == system_choice:
        print(f"Both players selected {user_choice}. it's a tie!")
    elif user_choice == 'Rock':
        if system_choice == 'Paper':
            print('Paper covers rock. You lose.')
        else:  # scissor
            print('Rock smashes Scissor. You win!')
    elif user_choice == 'Paper':
        if system_choice == 'Rock':
            print('Paper covers rock. You win!')
        else:
            print("Scissor cuts paper. you lose.")
    elif user_choice == 'Scissor':
        if system_choice == 'Rock':
            print('Rock smashes Scissor. You win!')
        else:
            print('Scissor cuts Paper. You win!')
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
