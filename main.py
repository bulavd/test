import pygame
from ball import Ball
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

f = pygame.font.SysFont('arial', 30)

w, h = 1820, 980
sc = pygame.display.set_mode((w, h))

bg = pygame.image.load('bg.png').convert()
score = pygame.image.load('score_fon.png').convert_alpha()
telega = pygame.image.load('telega.png').convert_alpha()
t_rect = telega.get_rect(centerx=w//2, bottom=h-5)

clock = pygame.time.Clock()
FPS = 60
game_score = 0

balls_data = ({'path': 'ball_lion.png', 'score': 100},
              {'path': 'ball_panda.png', 'score': 150},
              {'path': 'ball_pantera.png', 'score': 200})

balls_surf = [pygame.image.load(''+data['path']).convert_alpha() for data in balls_data]

balls = pygame.sprite.Group()


def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, w-20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)


createBall(balls)
speed = 10

def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            game_score += ball.score
            ball.kill()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > w-t_rect.width:
            t_rect.x = w-t_rect.width

    sc.blit(bg, (0, 0))
    balls.draw(sc)
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))
    sc.blit(telega, t_rect)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(h)
    collideBalls()
