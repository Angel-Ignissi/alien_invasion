import pygame


class Ship:
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Ининациализирует корабль (как прямоугольный объект) и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник (размеры и положение прямоугольника)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появится на середине нижней грани поверхности
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции на поверхности"""
        self.screen.blit(self.image, self.rect)
