import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определяем размеры экрана
WIDTH, HEIGHT = 1900, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Выбор Оружия")
background = pygame.image.load("sprites/backgtound/background.png")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка спрайтов
button1_image = pygame.image.load('sprites/ramki/ramka_dlia_tsiferki.png').convert_alpha()
button2_image = pygame.image.load('sprites/ramki/ramka_dlia_tsiferki.png').convert_alpha()
button3_image = pygame.image.load('sprites/ramki/ramka_dlia_tsiferki.png').convert_alpha()
weapon_image = pygame.image.load('sprites/main_character.png').convert_alpha()  # Спрайт для оружия


# Классы кнопок
class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Создание кнопок
button1 = Button(button1_image, 200, 300)
button2 = Button(button2_image, 700, 300)
button3 = Button(button3_image, 1200, 300)

# Переменные состояния
show_weapon_selection = False

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button1.is_clicked(event.pos) or button2.is_clicked(event.pos) or button3.is_clicked(event.pos):
                show_weapon_selection = True

    screen.blit(background, (0, 0))

    if not show_weapon_selection:
        # Отрисовка кнопок
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
    else:
        # Отрисовка меню выбора оружия
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        screen.blit(pygame.image.load("sprites/weapons/fon_dlia_weapons.png"), (1260, 0))
        screen.blit(pygame.image.load("sprites/weapons/weapon_1_digl_for_vibor.png"), (1400, 52))
        screen.blit(pygame.image.load("sprites/weapons/weapon_2_AK_for_vibor.png"), (1400, 300))
        screen.blit(pygame.image.load("sprites/weapons/weapon_3_for_vibor.png"), (1400, 548))

        font = pygame.font.Font(None, 36)
        text = font.render('Запуск', True, WHITE)
        screen.blit(text, (WIDTH - 180, HEIGHT - 70))

    pygame.display.flip()  # Обновляем экран
