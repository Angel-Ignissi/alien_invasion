class Settings:
    """Класс для хранения всех настроек игры alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.width = 1200
        self.height = 800
        self.bg_color = (85, 104, 195)

        # Настройки корабля
        self.ship_speed = 1.5

        # Настройки снарядов
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
