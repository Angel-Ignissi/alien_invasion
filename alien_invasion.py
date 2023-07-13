import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает трудовые ресурсы"""
        pygame.init()

        # поверхность
        self.settings = Settings()
        # поверхность на весь экран для любого устройства
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')

        # корабль
        self.ship = Ship(self)  # здесь главная поверхность передается кораблю в качестве аргумента
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран и объекты на нем
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

    def _check_events(self):
        # цикл событий для отслеживания событий у клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


if __name__ == '__main__':
    # Создание экземпляра, запуск игры
    ai = AlienInvasion()
    ai.run_game()
