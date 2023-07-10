import pygame


class Ship:
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Ининициализирует корабль - прямоугольный объект и задает его начальное положение на поверхности"""
        # поверхность для размещения корабля
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # сам корабль
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # корабль рисуется на середине нижней грани поверхности

        # Флаг перемещения
        self.moving_right = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Рисует корабль в текущей позиции на поверхности"""
        # blit(что, где)
        self.screen.blit(self.image, self.rect)
