
import pygame
delay_duration =5  # مدة التأخير بالملي ثانية (100 ms)
fade_duration = 10  # مدة تأثير التلاشي
colors = {
    0: (255, 255, 255),   # White
    1: (255, 99, 132),   # Pink
    2: (54, 0, 255),       # Blue
    3: (153, 102, 255),     # Purple
    4: (255, 0, 127),     # Rose
    5: (0, 0, 0),         # Black
    6: (0, 255, 127),     # Cyan
    7: (139, 69, 19),     # Brown
    8:  (255, 159, 64),     # Orange
    9: (255, 206, 86),       # Dark Green
    10: (0, 0, 139),      # Dark Blue
    11: (54, 162, 235),  # Light Blue
    12:(187, 255, 0)  # Light Green
}

pygame.init()

# Screen dimensions
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# Define the size of each grid cell
cell_size = width // 8
def draw(board):
    screen.fill((255, 255, 255))

    # رسم الشبكة
    for row in range(8):
        for col in range(8):
            color = colors[board[row][col]]
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

            # خطوط الشبكة
            pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)

    pygame.display.flip()


def draw_with_fade(board, piece, x, y):
    """ إضافة تأثير التلاشي عند رسم القطعة """
    fade_steps = 10  # عدد مراحل التلاشي
    for step in range(1, fade_steps + 1):
        screen.fill((255, 255, 255))

        for row in range(8):
            for col in range(8):
                if x <= row < x + len(piece) and y <= col < y + len(piece[0]) and piece[row - x][col - y] != 0:
                    # تعديل لون القطعة أثناء التلاشي
                    color = colors[piece[row - x][col - y]]
                    faded_color = (color[0], color[1], color[2], int(255 * (step / fade_steps)))
                    pygame.draw.rect(screen, faded_color, (col * cell_size, row * cell_size, cell_size, cell_size))
                else:
                    color = colors[board[row][col]]
                    pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

                pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)

        pygame.display.flip()
        pygame.time.delay(fade_duration // fade_steps)