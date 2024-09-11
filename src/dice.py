import random

class Dice:
    def __init__(self):
        self.knuckle_faces = ['beholder', 'ghost', 'princess', 'knight', 'dragon']
        self.thumb_faces = self.knuckle_faces + ['orc']

    def roll(self):
        """Simulate rolling the four knuckles."""
        rolls = [(random.choice(self.knuckle_faces), 'knuckle') for _ in range(3)]
        rolls.append((random.choice(self.thumb_faces), 'thumb knuckle'))
        return rolls
