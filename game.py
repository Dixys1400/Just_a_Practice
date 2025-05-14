import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Блоки
block_size = 50
blocks = []

# Игровой персонаж
player_width = 40
player_height = 40
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

# Переменные для отслеживания состояния игры
blocks_visible = True  # Блоки видимы по умолчанию
last_reset_time = 0  # Время последнего сброса блока
game_over_time = 0  # Время начала экрана с сообщением "Вы проиграли"

# Шрифты
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Функция для проверки столкновений с блоками
def check_collision(player_x, player_y, blocks):
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for block in blocks:
        block_rect = pygame.Rect(block[0], block[1], block_size, block_size)
        if player_rect.colliderect(block_rect):
            return True
    return False

# Главный игровой цикл
running = True
while running:
    screen.fill(WHITE)  # Очистить экран

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Если игра окончена, выводим сообщение
    if not blocks_visible and time.time() - game_over_time < 3:
        # Сообщение о проигрыше
        game_over_text = font.render("Вы проиграли!", True, RED)
        restart_text = small_font.render("Нажмите любую клавишу, чтобы начать заново", True, BLACK)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
        screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 50))
    else:
        # Управление движением игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Генерация случайных блоков
        if random.random() < 0.05 and blocks_visible:
            block_x = random.randint(0, screen_width - block_size)
            block_y = random.randint(0, screen_height - block_size)
            blocks.append((block_x, block_y))

        # Проверка на столкновение
        if check_collision(player_x, player_y, blocks):
            # Если столкновение, сбрасываем игрока в исходную позицию и делаем блоки невидимыми на 3 секунды
            player_x = screen_width // 2
            player_y = screen_height // 2
            blocks_visible = False  # Блоки исчезают
            game_over_time = time.time()  # Запоминаем время, когда началась "игра"
            blocks.clear()  # Удаляем все блоки, чтобы они исчезли

        # Отображение блоков, если они видимы
        if blocks_visible:
            for block in blocks:
                pygame.draw.rect(screen, GREEN, (block[0], block[1], block_size, block_size))

        # Отображение игрока
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

        # Проверка, прошло ли 3 секунды
        if not blocks_visible and time.time() - game_over_time >= 3:
            blocks_visible = True  # Блоки снова появляются через 3 секунды

    pygame.display.update()  # Обновить экран

    # Ограничение FPS
    pygame.time.Clock().tick(30)

# Завершение игры
pygame.quit()
