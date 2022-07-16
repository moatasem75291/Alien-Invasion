class GameStats:
    """Track statistics for alien invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.rest_stats()

        # start game in an inactive state.
        self.game_active = False

        # start an alien invasion in an active state.
        self.game_active = True

        # high score should never be reset.
        self.high_score = 0

    def rest_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
