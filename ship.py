import pygame


class Ship:
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Ининициализирует корабль - прямоугольный объект и задает его начальное положение на поверхности"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # изображение корабля
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # корабль рисуется на середине нижней грани поверхности

        # сохранение вещественной координаты корабля
        self.x = float(self.rect.x)

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # Обновляется атрибут x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции на поверхности"""
        # blit(что, где)
        self.screen.blit(self.image, self.rect)
