"""A small example class for learning object-oriented Python.

A class is a blueprint. An *instance* (also called an object) is one
concrete player built from that blueprint.
"""


class Player:
    """A basketball player with season box-score totals."""

    def __init__(self, name, team, points, games):
        # These are *properties* (also called attributes). Each instance
        # stores its own values on `self`.
        self.name = name
        self.team = team
        self.points = points
        self.games = games

    def points_per_game(self):
        """A *method*: a function that belongs to the class.

        It uses the instance's own points and games to compute PPG.
        """
        if self.games == 0:
            return 0.0
        return self.points / self.games

    def summary(self):
        """Return a one-line description of this player."""
        return (
            f"{self.name} ({self.team}) scored {self.points} points "
            f"in {self.games} games ({self.points_per_game():.1f} PPG)."
        )


if __name__ == "__main__":
    # This block only runs if you execute `python player.py` directly.
    demo = Player("Demo Player", "Training Team", 420, 20)
    print(demo.summary())
