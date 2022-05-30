class Stats:
    """Stats checking"""

    def __init__(self):
        """Stats init"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """Stats, changing while playing"""
        self.hp_left = 10
        self.score = 0
        self.bulletsNum = 30

