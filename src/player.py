from src.dice import Dice

class Player:
    def __init__(self, name):
        self.name = name
        self.rolls = []
        self.score = 0

    def roll_knuckles(self, dice):
        self.rolls = dice.roll()

    def display_roll(self):
        print(f"{self.name} rolled:")
        for rune, knuckle_type in self.rolls:
            print(f"  - {knuckle_type.capitalize()} shows a {rune.capitalize()}")

class HumanPlayer(Player):
    def roll_knuckles(self, dice):
        input(f"{self.name}, press any key to roll the knuckles...")
        super().roll_knuckles(dice)

class ComputerPlayer(Player):
    def roll_knuckles(self, dice):
        print(f"{self.name} is rolling the knuckles...")
        super().roll_knuckles(dice)
