from game_brain import Brain
from logo import logo
import random


b = Brain()
game_on = True
while game_on:
    print(logo)
    b.player_one_name = str(input("Player one's name (or q to quit): "))
    if b.player_one_name == "q":
        print("See you next time!!")
        game_on = False
        continue
    b.player_two_name = str(input("Player two's name (write c if playing against computer): "))
    x_or_o = False
    while not x_or_o:
        b.player_one_char = input(f"{b.player_one_name}, choose X or O: ").upper()
        if b.player_one_char == "O":
            b.player_two_char = "X"
            x_or_o = True
        elif b.player_one_char == "X":
            b.player_two_char = "O"
            x_or_o = True
        else:
            print("Please choose either X or O")

    # handle errors and choices
    print(f"{b.player_one_name} has {b.player_one_char} and {b.player_two_name} has {b.player_two_char}. ")
    print(b.game_board)
    round_ = True
    while round_:
        turn = True
        choice = input(f"{b.player_one_name}, place your {b.player_one_char}. (Example: a2): ")
        is_valid = b.check_location(choice)
        if is_valid:
            if b.already_chosen(choice):
                continue
            b.add_choice(choice, b.player_one_char)
            b.update_board()
            winner = b.check_winner()
            if not winner:
                round_ = False
                b.reset()
                continue
            if b.player_two_name == "c":
                while turn:
                    choice = random.choice(list(b.positions.keys()))
                    is_valid = b.check_location(choice)
                    if is_valid:
                        if b.already_chosen(choice):
                            continue
                        b.add_choice(choice, b.player_two_char)
                        b.update_board()
                        winner = b.check_winner()
                        if not winner:
                            round_ = False
                            b.reset()
                            turn = False
                            continue
                        turn = False
                    else:
                        continue
            while turn:
                choice = input(f"{b.player_two_name}, place your {b.player_two_char}. (Example: a2): ")
                is_valid = b.check_location(choice)
                if is_valid:
                    if b.already_chosen(choice):
                        continue
                    b.add_choice(choice, b.player_two_char)
                    b.update_board()
                    winner = b.check_winner()
                    if not winner:
                        round_ = False
                        b.reset()
                        continue
                    turn = False
                else:
                    continue
        else:
            continue

