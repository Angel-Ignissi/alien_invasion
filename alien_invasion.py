import sys

import pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает трудовые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            # (цикл событий для прослушивания событий у калвиатуры и мыши)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == '__main__':
    # Созздание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()