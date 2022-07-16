import pygame


class Settings:
    """A class to store all settings for alien invasion"""
    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (251, 251, 251)
        self.icon = pygame.image.load("images\image.jpg")
        # ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_color = (216, 32, 41)
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_allowed = 5
        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # how quickly the game speeds up
        self.speedup_scale = 1.1
        # how quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 3.5
        self.alien_speed = 2

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
