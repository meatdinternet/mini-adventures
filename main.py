import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Sprite Adventure")

clock = pygame.time.Clock()

sprite = pygame.Rect(375, 275, 50, 50)
speed = 5
color = (0, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sprite.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite.x += speed
    if keys[pygame.K_UP]:
        sprite.y -= speed
    if keys[pygame.K_DOWN]:
        sprite.y += speed

    sprite.x = max(0, min(sprite.x, WIDTH - sprite.width))
    sprite.y = max(0, min(sprite.y, HEIGHT - sprite.height))

    if sprite.left == 0:
        color = (255, 0, 0)     
    elif sprite.right == WIDTH:
        color = (0, 0, 255)     
    elif sprite.top == 0:
        color = (255, 255, 0)    
    elif sprite.bottom == HEIGHT:
        color = (255, 0, 255)  
    else:
        color = (0, 255, 0)  

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, color, sprite)


    outline_rect = sprite.inflate(20, 20)
    pygame.draw.rect(screen, (255, 255, 255), outline_rect, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()