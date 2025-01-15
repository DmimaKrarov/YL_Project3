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
fon_dlia_knopok = pygame.image.load("sprites/fon_dlia_knopki.png")
background = pygame.image.load("sprites/background.png")

# Определение областей кнопок с помощью прямоугольников
start_button = pygame.Rect(60, 400, 450, 100)  # Кнопка 'Начать игру'
shop_button = pygame.Rect(60, 550, 450, 100)  # Кнопка 'Начать игру'
exit_button = pygame.Rect(60, 700, 450, 100)  # Кнопка 'Выход'


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
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь закрыл окно
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Если нажата левая кнопка мыши
            if start_button.collidepoint(event.pos):
                print("Скибиди доп доп ес ес")  # Здесь следует добавить логику для начала игры
            if shop_button.collidepoint(event.pos):
                print("Магазик")  # Здесь следует добавить логику для магаза
            elif exit_button.collidepoint(event.pos):
                pygame.quit()  # Выходим из Pygame при нажатии на 'Выход'
                sys.exit()  # Завершаем программу

    screen.blit(background, (0, 0))  # Рисовашкаем задний фон
    draw_button(fon_dlia_knopok, start_button, "Играть")  # Рисуем кнопку с изображением
    draw_button(fon_dlia_knopok, shop_button, "Магазин")  # Рисуем кнопку с изображением
    draw_button(fon_dlia_knopok, exit_button, 'Выход')  # Можно использовать разные изображения для разных кнопок

    draw_text("Яндекс лицей.", font, (0, 0, 0), screen, 400, 175)  # Текст Названия игры
    draw_text("Закулисье.", font, (0, 0, 0), screen, 400, 275)  # Текст Названия игры

    pygame.display.flip()  # Обновляем экран
    pygame.time.Clock().tick(FPS)  # Ограничиваем частоту кадров

pygame.quit()  # Завершаем Pygame
