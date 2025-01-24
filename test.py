import asyncio
import time

import pygame  # Импортируем библиотеку Pygame
import sys  # Импортируем модуль sys для управления завершением программы

# Инициализация Pygame
pygame.init()  # Запускаем Pygame

# Константы настройки
WIDTH, HEIGHT = 1900, 1000  # Ширина и высота окна игры в пикселях
WHITE = (255, 255, 255)  # Цвет фона (белый)
FONT_COLOR = (0, 0, 0)  # Цвет шрифта (черный)
FPS = 60  # Частота кадров (frames per second)

# Создание окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Устанавливаем размеры окна
pygame.display.set_caption("Стартовое меню")  # Устанавливаем заголовок окна

# Настройка шрифтов
font = pygame.font.SysFont('Comic Sans MS', 74, italic=True)  # Основной шрифт для кнопок

# Загрузка изображения для кнопки
fon_dlia_knopok = pygame.image.load("sprites/ramki/fon_dlia_knopki.png")
background = pygame.image.load("sprites/backgtound/background.png")
background_crazy = pygame.image.load("sprites/backgtound/background_crazy.png")

# Определение областей кнопок с помощью прямоугольников
start_button = pygame.Rect(60, 520, 450, 100)  # Кнопка 'Начать игру'
shop_button = pygame.Rect(60, 670, 450, 100)  # Кнопка 'Начать игру'
exit_button = pygame.Rect(60, 820, 450, 100)  # Кнопка 'Выход'




# Функция для отрисовки основной меню
def draw_main_menu():
    screen.fill(WHITE)  # Заполняем фон
    screen.blit(background, (0, 0))  # Отрисуем задний фон
    pygame.draw.rect(screen, FONT_COLOR, start_button)  # Кнопка 'Начать игру'
    pygame.draw.rect(screen, FONT_COLOR, shop_button)  # Кнопка 'Магазин'
    pygame.draw.rect(screen, FONT_COLOR, exit_button)  # Кнопка 'Выход'
    text_start = font.render('Начать игру', True, FONT_COLOR)  # Текст кнопки
    text_shop = font.render('Магазин', True, FONT_COLOR)  # Текст кнопки
    text_exit = font.render('Выход', True, FONT_COLOR)  # Текст кнопки
    screen.blit(text_start, (start_button.x + 20, start_button.y + 20))  # Отрисуем текст кнопки
    screen.blit(text_shop, (shop_button.x + 20, shop_button.y + 20))  # Отрисуем текст кнопки
    screen.blit(text_exit, (exit_button.x + 20, exit_button.y + 20))  # Отрисуем текст кнопки


# Функция для отрисовки выбора оружия
def draw_weapon_selection():
    screen.fill(WHITE)  # Заполняем фон
    screen.blit(background, (0, 0))  # Отрисуем задний фон
    # Отрисовка трех кнопок
    button1 = pygame.Rect(60, 520, 450, 100)  # Кнопка 1
    button2 = pygame.Rect(60, 670, 450, 100)  # Кнопка 2
    button3 = pygame.Rect(60, 820, 450, 100)  # Кнопка 3
    pygame.draw.rect(screen, FONT_COLOR, button1)
    pygame.draw.rect(screen, FONT_COLOR, button2)
    pygame.draw.rect(screen, FONT_COLOR, button3)
    text1 = font.render('1', True, FONT_COLOR)
    text2 = font.render('2', True, FONT_COLOR)
    text3 = font.render('3', True, FONT_COLOR)
    screen.blit(text1, (button1.x + 20, button1.y + 20))
    screen.blit(text2, (button2.x + 20, button2.y + 20))
    screen.blit(text3, (button3.x + 20, button3.y + 20))

    # Отрисовка меню выбора оружия - можно настроить
    weapon_selection_rect = pygame.Rect(500, 100, 800, 600)  # Прямоугольник для меню выбора оружия
    pygame.draw.rect(screen, (0, 0, 0), weapon_selection_rect)
    # Здесь вы можете добавить логику для отрисовки выбора оружия и кнопки "Старт"


def draw_text(text, font, color, surface, x, y):
    """Функция для рисования текста на экране."""
    textobj = font.render(text, True, color)  # Создаем текстовый объект
    textrect = textobj.get_rect()  # Получаем прямоугольник текста
    textrect.center = (x, y)  # Центрируем текст по заданным координатам
    surface.blit(textobj, textrect)  # Отображаем текст на экране


def draw_button(image, rect, text):
    """Функция для рисования кнопки с изображением."""
    # Проверяем, находится ли курсор мыши над кнопкой
    if rect.collidepoint(pygame.mouse.get_pos()):
        # Если мышь над кнопкой, затемняем изображение (можно заменить на другое изображение)
        tinted_image = pygame.Surface(rect.size)  # Создаем поверхность
        tinted_image.fill((150, 150, 150))  # Заполняем серым цветом
        # Накладываем изображение на эту поверхность
        tinted_image.blit(image, (0, 0), special_flags=pygame.BLEND_MULT)
        screen.blit(tinted_image, rect.topleft)  # Выводим затемненное изображение на экран
    else:
        screen.blit(image, rect.topleft)  # Выводим обычное изображение на экран

    # Создаем текстовую поверхность для кнопки
    text_surface = font.render(text, True, FONT_COLOR)
    # Вычисляем прямоугольник текста, чтобы центрировать его на кнопке
    text_rect = text_surface.get_rect(center=rect.center)
    # Рисуем текст на экране
    screen.blit(text_surface, text_rect)


# Основной игровой цикл
def main():
    paint = -40
    running = True
    show_main_menu = True  # Отображать ли основное меню
    show_weapon_selection = False  # Отображать ли выбор оружия
    while running:
        paint += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if show_main_menu:
                    if start_button.collidepoint(event.pos):
                        show_main_menu = False
                        show_weapon_selection = True

        if show_main_menu:
            draw_main_menu()
        elif show_weapon_selection:
            draw_weapon_selection()

        pygame.display.flip()  # Обновляем экран
        pygame.time.Clock().tick(FPS)  # Ограничиваем частоту кадров


if __name__ == '__main__':
    main()
