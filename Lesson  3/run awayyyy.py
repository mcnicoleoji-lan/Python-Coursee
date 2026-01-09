import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer with BOSS 👑")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
PURPLE = (150, 50, 200)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 64)

# Player
player = pygame.Rect(100, 500, 40, 60)
vel_x = 0
vel_y = 0
speed = 5
jump = 15
gravity = 0.8
on_ground = False
health = 3

# Platforms
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
    pygame.Rect(200, 450, 200, 20),
    pygame.Rect(500, 350, 200, 20)
]

# Coins
coins = [
    pygame.Rect(240, 410, 20, 20),
    pygame.Rect(580, 310, 20, 20)
]

# BOSS
boss = pygame.Rect(500, 290, 100, 60)
boss_health = 5
boss_dir = 1
boss_speed = 2
boss_alive = True

score = 0
game_over = False
you_win = False

while True:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if game_over:
        text = big_font.render("GAME OVER 😵", True, RED)
        screen.blit(text, (WIDTH//2 - 180, HEIGHT//2))
        pygame.display.update()
        continue

    if you_win:
        text = big_font.render("YOU BEAT THE BOSS 👑", True, PURPLE)
        screen.blit(text, (WIDTH//2 - 240, HEIGHT//2))
        pygame.display.update()
        continue

    # Input
    vel_x = 0
    if keys[pygame.K_LEFT]:
        vel_x = -speed
    if keys[pygame.K_RIGHT]:
        vel_x = speed
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = -jump
        on_ground = False

    # Physics
    vel_y += gravity
    player.x += vel_x
    player.y += vel_y

    # Platform collision
    on_ground = False
    for p in platforms:
        if player.colliderect(p) and vel_y > 0:
            player.bottom = p.top
            vel_y = 0
            on_ground = True

    # Coins
    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

    # Boss logic
    if boss_alive:
        boss.x += boss_speed * boss_dir
        if boss.left < 400 or boss.right > 780:
            boss_dir *= -1

        if player.colliderect(boss):
            if vel_y > 0 and player.bottom <= boss.top + 20:
                boss_health -= 1
                vel_y = -10
                if boss_health <= 0:
                    boss_alive = False
                    you_win = True
            else:
                health -= 1
                player.x -= 50
                if health <= 0:
                    game_over = True

    # Draw
    for p in platforms:
        pygame.draw.rect(screen, GREEN, p)

    for c in coins:
        pygame.draw.circle(screen, GOLD, c.center, 10)

    pygame.draw.rect(screen, BLUE, player)

    if boss_alive:
        pygame.draw.rect(screen, PURPLE, boss)
        pygame.draw.rect(screen, RED, (boss.x, boss.y - 10, boss_health * 20, 5))

    # UI
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Health: {health}", True, BLACK), (10, 40))
    screen.blit(font.render("Boss HP", True, BLACK), (boss.x, boss.y - 30))

    pygame.display.update()
