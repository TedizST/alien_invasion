import json


class GameStats:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.score = 0
        self.level = 1

        # Рекорд не должен сбрасываться.
        self.high_score = self.get_stored_high_score()

        # Игра запускается в неактивном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit

    @staticmethod
    def get_stored_high_score():
        try:
            with open('high_score.json') as file_object:
                high_score = json.load(file_object)
        except FileNotFoundError:
            with open('high_score.json') as file_object:
                json.dump(0, file_object)
            high_score = 0
        finally:
            return high_score
