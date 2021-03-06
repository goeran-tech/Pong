import pygame, sys, random

def ball_movement():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_restart()
        opponent_score += 1
    if ball.right >= SCREEN_WIDTH:
        ball_restart()
        player_score += 1


    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        ball_speed_y *= random.choice((1, -1))

def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

def opponent_movement():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong') 

ball = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2-15, 30, 30)
player = pygame.Rect(10, SCREEN_HEIGHT/2-70, 10, 140)
opponent = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2-70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

ball_speed = 15
ball_speed_x = ball_speed * random.choice((1, -1))
ball_speed_y = ball_speed * random.choice((1, -1))
opponent_speed = 15
player_speed = 0

player_score = 0
opponent_score = 0

font = pygame.font.Font('freesansbold.ttf', 64)

while True:
    playerText = font.render(str(player_score), True, light_grey, bg_color) 
    playerTextRect = playerText.get_rect()
    playerTextRect.center = (SCREEN_WIDTH/3, 40)

    opponentText = font.render(str(opponent_score), True, light_grey, bg_color) 
    opponentTextRect = opponentText.get_rect()
    opponentTextRect.center = (SCREEN_WIDTH/3*2, 40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed += 15
            if event.key == pygame.K_w:
                player_speed -= 15

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed -= 15
            if event.key == pygame.K_w:
                player_speed += 15

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    ball_movement()
    player_movement()
    opponent_movement()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    screen.blit(playerText, playerTextRect)
    screen.blit(opponentText, opponentTextRect)
    
    pygame.display.flip()
    clock.tick(30)