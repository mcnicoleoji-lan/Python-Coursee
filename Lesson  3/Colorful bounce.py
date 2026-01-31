import pygame
import random

# Initialize Pygame
pygame.init()
# Custom event IDs
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
# Define basic colors using pygame.Color
# Background colors
PINK = pygame.Color('pink')
LIGHTPINK = pygame.Color('lightpink')
DARKPINK = pygame.Color('darkpink')

# Sprite colors
PURPLE = pygame.Color('purple')
MAGENTA = pygame.Color('magenta')
PEACH = pygame.Color('peachpuff')
WHITE = pygame.Color('white')
# Object class
class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        def change_color(self):
            self.image.fill(random.choice([PURPLE, MAGENTA, PEACH, WHITE]))

def change_background_color():
    global bg_color
    bg_color = random.choice([PINK, LIGHTPINK, DARKPINK])
all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")
bg_color = PINK
screen.fill(bg_color)
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()
            all_sprites_list.update()
screen.fill(bg_color)
all_sprites_list.draw(screen)

pygame.display.flip()
clock.tick(240)

pygame.quit()
