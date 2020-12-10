import pygame

if __name__ == '__main__':

    class Board:
        # создание поля
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.board = [[0] * width for _ in range(height)]
            # значения по умолчанию
            self.left = 10
            self.top = 10
            self.cell_size = 30

        # настройка внешнего вида
        def set_view(self, left, top, cell_size):
            self.left = left
            self.top = top
            self.cell_size = cell_size

        def render(self, screen):
            for y in range(self.height):
                for x in range(self.width):
                    pygame.draw.rect(screen,
                                     '#FFFFFF',
                                     [self.left + self.cell_size * x, self.top + self.cell_size * y,
                                      self.cell_size, self.cell_size],
                                     1)

        def get_cell(self, mouse_pos):
            if mouse_pos[0] < self.left or mouse_pos[0] > self.left + self.cell_size * self.width or \
                    mouse_pos[1] < self.top or mouse_pos[1] > self.top + self.cell_size * self.height:
                return None, None
            else:
                number_cell_x = (mouse_pos[0] - self.left) // self.cell_size
                number_cell_y = (mouse_pos[1] - self.top) // self.cell_size
            return number_cell_x, number_cell_y

        def get_click(self, mouse_pos):
            cell = self.get_cell(mouse_pos)
            self.on_click(cell)

        def on_click(self, cell):
            print(cell[0], cell[1])


    pygame.init()
    pygame.display.set_caption('Инициализация игры')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    fps = 50  # количество кадров в секунду
    clock = pygame.time.Clock()
    board = Board(5, 7)
    board.set_view(10, 10, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
