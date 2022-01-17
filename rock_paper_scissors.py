import random

rps_list = ("Rock", "Paper", "Scissors")
select_list = ("1", "2", "3", "4")

def comp():
    user_score = int(0)
    cpu_score = int(0)
    tied_score = int(0)
    while True:
        player1 = input("Input your selection: ").capitalize()
        rps_random = random.choice(rps_list).capitalize()
        if player1 not in rps_list:
            print("Invalid selection!")
        elif player1 in rps_list:
            print("\nRock!\nPaper!\nScissors!\nShoot!\n")
            print(player1 + " vs. " + rps_random)

            print("--------------------")

            if (player1 == "Rock") and (rps_random == "Rock"):
                print("It's a tie!")
                tied_score += 1
            elif (player1 == "Rock") and (rps_random == "Paper"):
                print("You lose!")
                cpu_score += 1
            elif (player1 == "Rock") and (rps_random == "Scissors"):
                print("You win!")
                user_score += 1
            elif (player1 == "Scissors") and (rps_random == "Scissors"):
                print("It's a tie!")
                tied_score += 1
            elif (player1 == "Scissors") and (rps_random == "Rock"):
                print("You lose")
                cpu_score += 1
            elif (player1 == "Scissors") and (rps_random == "Paper"):
                print("You win!")
                user_score += 1
            elif (player1 == "Paper") and (rps_random == "Paper"):
                print("It's a tie!")
                tied_score += 1
            elif (player1 == "Paper") and (rps_random == "Scissors"):
                print("You lose!")
                cpu_score += 1
            elif (player1 == "Paper") and (rps_random == "Rock"):
                print("You win!")
                user_score += 1
            print(f"\nCPU score: {cpu_score}\nUser score: {user_score}\nTied score: {tied_score}")
            play_again = input("\nDo you want to play again: ")
            if play_again.capitalize() == "No":
                break

def pvp():
    player1_score = int(0)
    player2_score = int(0)
    tied_score = int(0)
    while True:
        result1 = False
        result2 = False
        while result1 == False:
            player1 = input("Input your selection for player 1: ").capitalize()
            if player1 not in rps_list:
                print("Invalid selection!")
            else:
                result1 = True
        while result2 == False:
            player2 = input("Input your selection for player 2: ").capitalize()
            if player2 not in rps_list:
                print("Invalid selection!")
            else:
                result2 = True
        if (player1 and player2) in rps_list:
            print("\nRock!\nPaper!\nScissors!\nShoot!\n")
            print(player1 + " vs. " + player2)

            print("--------------------")

            if (player1 == "Rock") and (player2 == "Rock"):
                print("It's a tie!")
                tied_score += 1
            elif (player1 == "Rock") and (player2 == "Paper"):
                print("Player 2 wins!")
                player2_score += 1
            elif (player1 == "Rock") and (player2 == "Scissors"):
                print("Player 1 wins!")
                player1_score += 1
            elif (player1 == "Scissors") and (player2 == "Scissors"):
                print("It's a tie!")
                tied_score += 1
            elif (player1 == "Scissors") and (player2 == "Rock"):
                print("Player 2 wins!")
                player2_score += 1
            elif (player1 == "Scissors") and (player2 == "Paper"):
                print("Player 1 wins!")
                player1_score += 1
            elif (player1 == "Paper") and (player2 == "Paper"):
                print("It's a tie!")
                tied_score += 1
            elif (player1 == "Paper") and (player2 == "Scissors"):
                print("Player 2 wins!")
                player2_score += 1
            elif (player1 == "Paper") and (player2 == "Rock"):
                print("Player 1 wins!")
                player1_score += 1
            print(f"Player 1 score: {player1_score}\nPlayer 2 score: {player2_score}\nTied score: {tied_score}")
            play_again = input("\nDo you want to play again: ")
            if play_again.capitalize() == "No":
                break

def wargames():
    cpu1_score = int(0)
    cpu2_score = int(0)
    tied_score = int(0)
    while True:
        rps_random1 = random.choice(rps_list).capitalize()
        rps_random2 = random.choice(rps_list).capitalize()
        print("\nRock!\nPaper!\nScissors!\nShoot!\n")
        print(rps_random1 + " vs. " + rps_random2)

        print("--------------------")

        if (rps_random1 == "Rock") and (rps_random2 == "Rock"):
            print("It's a tie!")
            tied_score += 1
        elif (rps_random1 == "Rock") and (rps_random2 == "Paper"):
            print("CPU 2 wins!")
            cpu2_score += 1
        elif (rps_random1 == "Rock") and (rps_random2 == "Scissors"):
            print("CPU 1 wins!")
            cpu1_score += 1
        elif (rps_random1 == "Scissors") and (rps_random2 == "Scissors"):
            print("It's a tie!")
            tied_score += 1
        elif (rps_random1 == "Scissors") and (rps_random2 == "Rock"):
            print("CPU 2 wins!")
            cpu2_score += 1
        elif (rps_random1 == "Scissors") and (rps_random2 == "Paper"):
            print("CPU 1 wins!")
            cpu1_score += 1
        elif (rps_random1 == "Paper") and (rps_random2 == "Paper"):
            print("It's a tie!")
            tied_score += 1
        elif (rps_random1 == "Paper") and (rps_random2 == "Scissors"):
            print("CPU 2 wins!")
            cpu2_score += 2
        elif (rps_random1 == "Paper") and (rps_random2 == "Rock"):
            print("CPU 2 wins!")
            cpu2_score += 1
        print(f"\nCPU1 score: {cpu1_score}\nCPU2 score: {cpu2_score}\nTied score: {tied_score}")
        play_again = input("\nDo you want to play again: ")
        if play_again.capitalize() == "No":
            break

print("\nWelcome to the Rock, Paper, Scissors game!")

main_menu = True
while main_menu == True:
    print("Select who you want to battle:\nPress 1 for Player vs. CPU\nPress 2 for Player vs. Player\nPress 3 for CPU vs. CPU\nPress 4 to exit.")
    user_select = input("Enter: ")
    if user_select in select_list:
        if user_select == "1":
            comp()
        elif user_select == "2":
            pvp()
        elif user_select == "3":
            wargames()
        else:
            main_menu = False
    else:
        print("Invalid input\n")