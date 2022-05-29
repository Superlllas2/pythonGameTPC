class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """статистика, изменяющаяся во время игры"""
        self.hp_left = 10
        self.score =0