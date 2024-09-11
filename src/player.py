class Player:
    def __init__(self, name):
        self.name = name
        self.rolls = []
        self.score = 0
        self.rune_values = {
            'ghost': 0,
            'beholder': 1,
            'princess': 2,
            'knight': 2,
            'dragon': 3,
            'orc': 0
        }

    def roll_knuckles(self, dice):
        self.rolls = dice.roll()

    def display_roll(self):
        print(f"{self.name} rolled:")
        for rune, knuckle_type in self.rolls:
            print(f"  - {knuckle_type.capitalize()} shows a {rune.capitalize()}")

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def roll_knuckles(self, dice):
        input(f"{self.name}, press any key to roll the knuckles...")
        super().roll_knuckles(dice)

    def choose_target(self, candidates):
        """Let the human player choose whom to cancel."""
        print(f"{self.name}, you have multiple targets to cancel. Choose a target:")
        for i, candidate in enumerate(candidates, start=1):
            print(f"{i}. {candidate}")
        choice = int(input("Enter the number of the target you want to cancel: ")) - 1
        return candidates[choice]

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def roll_knuckles(self, dice):
        print(f"{self.name} is rolling the knuckles...")
        super().roll_knuckles(dice)
