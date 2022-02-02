class Brain:
    def __init__(self):
        self.game_board = "     1   2   3  " \
                          "\na  |___|___|___|\n" \
                          "b  |___|___|___|\n" \
                          "c  |___|___|___|"
        self.positions = {
            "a1": 22,
            "a2": 26,
            "a3": 30,
            "b1": 39,
            "b2": 43,
            "b3": 47,
            "c1": 56,
            "c2": 60,
            "c3": 64
        }
        self.player_one_name = ""
        self.player_two_name = "Computer"
        self.player_one_char = ""
        self.player_two_char = ""
        self.past_choices = []

    def add_choice(self, choice, char):
        self.past_choices.append(choice)
        b_lst = list(self.game_board)
        b_lst[self.positions[choice]] = char
        self.game_board = ""
        for char in b_lst:
            self.game_board += char

    def update_board(self):
        print(self.game_board)

    def already_chosen(self, choice):
        if choice in self.past_choices:
            print("Square already taken, please choose another. ")
            return True
        else:
            return False

    def check_location(self, choice):
        try:
            self.positions[choice]
        except KeyError:
            print("Please choose a valid location. ")
            return False
        else:
            return True

    def check_winner(self):
        player_one_past_choices = self.past_choices[::2]
        if "a1" in player_one_past_choices and "a2" in player_one_past_choices and "a3" in player_one_past_choices:
            print(f"{self.player_one_name} Wins!!")
            print("Play again?")
            return False
        if "b1" in player_one_past_choices and "b2" in player_one_past_choices and "b3" in player_one_past_choices:
            print(f"{self.player_one_name} Wins!!")
            print("Play again?")
            return False
        if "c1" in player_one_past_choices and "c2" in player_one_past_choices and "c3" in player_one_past_choices:
            print(f"{self.player_one_name} Wins!!")
            print("Play again?")
            return False
        if "a1" in player_one_past_choices and "b1" in player_one_past_choices and "c1" in player_one_past_choices:
            print(f"{self.player_one_name} Wins!!")
            print("Play again?")
            return False
        if "a2" in player_one_past_choices and "b2" in player_one_past_choices and "c2" in player_one_past_choices:
            print(f"{self.player_one_name} Wins!!")
            print("Play again?")
            return False
        if "a3" in player_one_past_choices and "b3" in player_one_past_choices and "c3" in player_one_past_choices:
            print(f"{self.player_one_name} Wins!!")
            print("Play again?")
            return False
        if "a1" in player_one_past_choices and "b2" in player_one_past_choices and "c3" in player_one_past_choices:
            print(f"{self.player_one_name} Wins!!")
            print("Play again?")
            return False
        if "a3" in player_one_past_choices and "b2" in player_one_past_choices and "c1" in player_one_past_choices:
            print(f"{self.player_one_name} Wins!!")
            print("Play again?")
            return False
        player_two_past_choices = self.past_choices[1::2]
        if "a1" in player_two_past_choices and "a2" in player_two_past_choices and "a3" in player_two_past_choices:
            print(f"{self.player_two_name} Wins!!")
            print("Play again?")
            return False
        if "b1" in player_two_past_choices and "b2" in player_two_past_choices and "b3" in player_two_past_choices:
            print(f"{self.player_two_name} Wins!!")
            print("Play again?")
            return False
        if "c1" in player_two_past_choices and "c2" in player_two_past_choices and "c3" in player_two_past_choices:
            print(f"{self.player_two_name} Wins!!")
            print("Play again?")
            return False
        if "a1" in player_two_past_choices and "b1" in player_two_past_choices and "c1" in player_two_past_choices:
            print(f"{self.player_two_name} Wins!!")
            print("Play again?")
            return False
        if "a2" in player_two_past_choices and "b2" in player_two_past_choices and "c2" in player_two_past_choices:
            print(f"{self.player_two_name} Wins!!")
            print("Play again?")
            return False
        if "a3" in player_two_past_choices and "b3" in player_two_past_choices and "c3" in player_two_past_choices:
            print(f"{self.player_two_name} Wins!!")
            print("Play again?")
            return False
        if "a1" in player_two_past_choices and "b2" in player_two_past_choices and "c3" in player_two_past_choices:
            print(f"{self.player_two_name} Wins!!")
            print("Play again?")
            return False
        if "a3" in player_two_past_choices and "b2" in player_two_past_choices and "c1" in player_two_past_choices:
            print(f"{self.player_two_name} Wins!!")
            print("Play again?")
            return False
        if len(self.past_choices) == 9:
            print("Looks like there was a tie!!")
            print("Play again?")
            return False
        else:
            return True

    def reset(self):
        self.game_board = "     1   2   3  " \
                          "\na  |___|___|___|\n" \
                          "b  |___|___|___|\n" \
                          "c  |___|___|___|"
        self.past_choices = []
        return False




