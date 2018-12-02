import random


def rock_paper_scissor():
    # Track wins and losses
    win = 0
    loss = 0
    while win < 3 and loss < 3:
        # Create dictionaries that denote player and computer choices
        duel = {1: "Scissors", 2: "Rock", 3: "Paper"}
        duel2 = {"Scissors": 1, "Rock": 2, "Paper": 3, "scissors": 1, "rock": 2, "paper": 3}

        # Computer choice 1-3 that will refer to 'duel' dictionary
        comp_guess = random.randint(1, 3)
        # User choice rock, paper, or scissors that will refer to 'duel2' dictionary
        user_guess = input("amiguel12: ")
        # Input validation
        while user_guess not in duel2:
            print("Invalid, must be rock, paper, or scissors.")
            user_guess = input("amiguel12: ")
        # Print computer choice where 1-3s value from 'duel' dictionary is displayed
        print("Computer:", duel.get(comp_guess))
        print("")

        # Exceptions for scissors vs paper as scissors is worth 1 and paper is worth 3
        if comp_guess == 3 and user_guess in ["Scissors", "scissors"]:
            print("Result: User wins round")
            win += 1
            print("Score:", win, "-", loss)
            print("-------------------------------------------------")
        elif comp_guess == 1 and user_guess in ["Paper", "paper"]:
            print("Result: Comp wins round")
            loss += 1
            print("Score:", win, "-", loss)
            print("-------------------------------------------------")
        # When comp choice > user
        elif comp_guess > duel2.get(user_guess):
            print("Result: Comp wins round")
            loss += 1
            print("Score:", win, "-", loss)
            print("-------------------------------------------------")
        # When comp choice < user
        elif comp_guess < duel2.get(user_guess):
            print("Result: User wins round")
            win += 1
            print("Score:", win, "-", loss)
            print("-------------------------------------------------")
        # When comp choice == user
        elif comp_guess == duel2.get(user_guess):
            print("Result: Tie")
            print("Score:", win, "-", loss)
            print("-------------------------------------------------")

        # Display once either loss or win == 3
        if loss == 3:
            print("The cpu clapped your cheeks")
        elif win == 3:
            print("You clapped the cpu's cheeks")

rock_paper_scissor()