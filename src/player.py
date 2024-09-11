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

class HumanPlayer(Player):
    def choose_target(self, candidates):
        """Let the human player choose whom to cancel."""
        return candidates[0]  # For simplicity, it can be adjusted to use input if necessary.

class ComputerPlayer(Player):
    def choose_target(self, candidates):
        """Computer randomly chooses an opponent to cancel."""
        return candidates[0]
