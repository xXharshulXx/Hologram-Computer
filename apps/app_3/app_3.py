'''import pygame
import sys
import os
import math
import time
from dotenv import load_dotenv

load_dotenv()
pygame.init()
mixer = pygame.mixer
mixer.init()

#SCREEN_WIDTH = 1920
#SCREEN_HEIGHT = 1080
#SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH',1920))
#SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT',1080))
#SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

info = pygame.display.Info()  # Get monitor info
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_BLUE = (173,216,230)
NAVY_BLUE = (20,20,40)
RED = (255,0,0)
BLUE = (0,0,255)


def play_sound(file_path):
    try:
        mixer.music.load(file_path)
        mixer.music.play()
    except pygame.error as e:
        print(f"Error playing sound {file_path}: {e}")


def map_coords(x,y):
    #mapped_x = (y/1080) * 1920
    #mapped_y = 1080 - ((x/1920) * 1080)
    return x,y


def space_invaders(screen):
    player_img = pygame.image.load("apps/app_3/player.png")
    invader1_img = pygame.image.load("apps/app_3/invader1.png")
    invader2_img = pygame.image.load("apps/app_3/invader2.png")


    player_scale = 8
    invader_scale = 3
    player_img = pygame.transform.scale(player_img,(int(player_img.get_width()*player_scale),int(player_img.get_height()*player_scale)))
    invader1_img = pygame.transform.scale(invader1_img,(int(invader1_img.get_width()*invader_scale),int(invader1_img.get_height()*invader_scale)))
    invader2_img = pygame.transform.scale(invader2_img,(int(invader2_img.get_width()*invader_scale),int(invader2_img.get_height()*invader_scale)))


    player = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT-player_img.get_height()-10, player_img.get_width(), player_img.get_height())
    bullets = []
    invaders = []
    invader_speed_x = 3
    bullet_speed = -10
    invader_direction = 1


    home_button_center = (60,50)
    home_button_radius = 50
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = map_coords(*event.pos)
                if math.hypot(x - home_button_center[0], y - home_button_center[1]) <= home_button_radius:
                    running = False
                
                else:
                    play_sound('./apps/app_3/laser.mp3')
                    bullets.append(pygame.Rect(player.centerx - 2.5, player.top - 10, 5, 10))
            

        screen.fill(BLACK)


        pygame.draw.circle(screen,NAVY_BLUE,home_button_center,home_button_radius)
        pygame.draw.circle(screen,LIGHT_BLUE,home_button_center,home_button_radius,5)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Home',True,WHITE)
        screen.blit(text_surface,text_surface.get_rect(center=home_button_center))

        pygame.display.flip()
        pygame.time.delay(10)


def brick_breaker(screen):
    paddle = pygame.Rect(SCREEN_WIDTH//2 - 75, SCREEN_HEIGHT - 50, 150, 20)
    ball = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 2, 20, 20)
    ball_dx,ball_dy = 7,-7


    bricks = [pygame.Rect(320+col*125,50+row*30,120,25)for row in range(5) for col in range(10)]


    home_button_center = (100,SCREEN_HEIGHT-100)
    home_button_radius = 50
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = map_coords(*event.pos)
                if math.hypot(x - home_button_center[0], y - home_button_center[1]) <= home_button_radius:
                    running = False
                else:
                    paddle.centerx = x


        ball.x += ball_dx
        ball.y += ball_dy


        screen.fill(BLACK)
        pygame.draw.rect(screen,WHITE,paddle)
        pygame.draw.ellipse(screen,BLUE,ball)
        for brick in bricks:
            pygame.draw.rect(screen,RED,brick)


        pygame.draw.circle(screen,NAVY_BLUE,home_button_center,home_button_radius)
        pygame.draw.circle(screen,WHITE,home_button_center,home_button_radius,5)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Home',True,WHITE)
        screen.blit(text_surface,text_surface.get_rect(center=home_button_center))

        pygame.display.flip()
        pygame.time.delay(10)


def run(screen):
    running = True
    circle_radius = 100
    space_invaders_button_center = (SCREEN_WIDTH//3, SCREEN_HEIGHT//2)
    brick_breaker_button_center = (2*SCREEN_WIDTH//3, SCREEN_HEIGHT//2)
    home_button_center = (50+circle_radius,SCREEN_HEIGHT-50-circle_radius)


    space_invaders_img = pygame.image.load("./apps/app_3/space_invaders.jpg")
    space_invaders_img = pygame.transform.scale(space_invaders_img,(2*circle_radius,2*circle_radius))

    brick_breaker_img = pygame.image.load("./apps/app_3/brick_breaker.jpg")
    brick_breaker_img = pygame.transform.scale(brick_breaker_img,(2*circle_radius,2*circle_radius))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = map_coords(*event.pos)


                if math.hypot(x - space_invaders_button_center[0], y - space_invaders_button_center[1]) <= circle_radius:
                    play_sound('./apps/app_3/game_start.mp3')
                    space_invaders(screen)

                elif math.hypot(x - brick_breaker_button_center[0], y - brick_breaker_button_center[1]) <= circle_radius:
                    play_sound('./apps/app_3/game_start.mp3')   
                    brick_breaker(screen)

                elif math.hypot(x - home_button_center[0], y - home_button_center[1]) <= circle_radius:
                    play_sound('./apps/app_3/back.wav')
                    running = False


        screen.fill(BLACK)


        screen.blit(space_invaders_img, (space_invaders_button_center[0]-circle_radius, space_invaders_button_center[1]-circle_radius))
        pygame.draw.circle(screen,WHITE,space_invaders_button_center,circle_radius,5)


        screen.blit(brick_breaker_img, (brick_breaker_button_center[0]-circle_radius, brick_breaker_button_center[1]-circle_radius))
        pygame.draw.circle(screen,WHITE,brick_breaker_button_center,circle_radius,5)


        pygame.draw.circle(screen,NAVY_BLUE,home_button_center,circle_radius)
        pygame.draw.circle(screen,WHITE,home_button_center,circle_radius,5)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Home',True,WHITE)
        screen.blit(text_surface,text_surface.get_rect(center=home_button_center))

        pygame.display.flip()
        pygame.time.delay(50)

if __name__ == '__main__':
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Arcade')
    run(screen)'''

import pygame
import sys
import os
import math
import time
from dotenv import load_dotenv

# ---------------- Setup ---------------- #
load_dotenv()
pygame.init()
mixer = pygame.mixer
mixer.init()

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_BLUE = (173,216,230)
NAVY_BLUE = (20,20,40)
RED = (255,0,0)
BLUE = (0,0,255)

# ---------------- Helpers ---------------- #
def play_sound(file_path):
    """Safely plays a sound if available"""
    try:
        if os.path.exists(file_path):
            mixer.music.load(file_path)
            mixer.music.play()
    except pygame.error as e:
        print(f"Error playing sound {file_path}: {e}")

def map_coords(x, y):
    """Simple coordinate mapper"""
    return x, y

# ========================================================= #
#                     SPACE INVADERS                        #
# ========================================================= #
def space_invaders(screen):
    try:
        player_img = pygame.image.load("apps/app_3/player.png").convert_alpha()
        invader_img = pygame.image.load("apps/app_3/invader1.png").convert_alpha()
    except Exception as e:
        print("Image load error (space_invaders):", e)
        player_img = None
        invader_img = None

    # scale images or fallback
    player_scale = 4
    invader_scale = 2
    if player_img:
        player_img = pygame.transform.scale(player_img,
                    (int(player_img.get_width()*player_scale),
                     int(player_img.get_height()*player_scale)))
    if invader_img:
        inv_w = int(invader_img.get_width()*invader_scale)
        inv_h = int(invader_img.get_height()*invader_scale)
        invader_img = pygame.transform.scale(invader_img, (inv_w, inv_h))
    else:
        inv_w, inv_h = 40, 30

    # player setup
    player = pygame.Rect(SCREEN_WIDTH//2 - 30, SCREEN_HEIGHT - 100, 60, 60)
    bullets = []
    invaders = []
    invader_speed_x = 2
    invader_direction = 1
    invader_drop = 20
    bullet_speed = -12

    # create grid of invaders
    rows, cols = 3, 8
    margin_x, margin_y = 80, 80
    spacing_x = (SCREEN_WIDTH - margin_x*2) // cols
    spacing_y = 60
    for r in range(rows):
        for c in range(cols):
            invaders.append(pygame.Rect(margin_x + c * spacing_x, margin_y + r * spacing_y, inv_w, inv_h))

    clock = pygame.time.Clock()
    home_button_center = (60, 50)
    home_button_radius = 50
    running = True

    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = map_coords(*event.pos)
                if math.hypot(mx - home_button_center[0], my - home_button_center[1]) <= home_button_radius:
                    running = False
                    break
                else:
                    bullets.append(pygame.Rect(player.centerx - 3, player.top - 10, 6, 10))
                    play_sound('./apps/app_3/laser.mp3')

        # player movement (arrow keys)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 8
        if keys[pygame.K_RIGHT]:
            player.x += 8
        player.x = max(0, min(SCREEN_WIDTH - player.width, player.x))

        # move bullets
        for b in bullets[:]:
            b.y += bullet_speed
            if b.bottom < 0:
                bullets.remove(b)

        # move invaders
        if invaders:
            leftmost = min(i.x for i in invaders)
            rightmost = max(i.right for i in invaders)
            if rightmost >= SCREEN_WIDTH - 10 and invader_direction == 1:
                invader_direction = -1
                for i in invaders:
                    i.y += invader_drop
            elif leftmost <= 10 and invader_direction == -1:
                invader_direction = 1
                for i in invaders:
                    i.y += invader_drop

            for i in invaders:
                i.x += invader_speed_x * invader_direction

        # check bullet collisions
        for b in bullets[:]:
            for i in invaders[:]:
                if b.colliderect(i):
                    bullets.remove(b)
                    invaders.remove(i)
                    play_sound('./apps/app_3/invader_kill.wav')
                    break

        # draw
        screen.fill(BLACK)
        for inv in invaders:
            if invader_img:
                screen.blit(invader_img, (inv.x, inv.y))
            else:
                pygame.draw.rect(screen, (0,200,0), inv)
        if player_img:
            screen.blit(player_img, (player.x, player.y))
        else:
            pygame.draw.rect(screen, WHITE, player)
        for b in bullets:
            pygame.draw.rect(screen, (255,255,0), b)

        # Home button
        pygame.draw.circle(screen, NAVY_BLUE, home_button_center, home_button_radius)
        pygame.draw.circle(screen, LIGHT_BLUE, home_button_center, home_button_radius, 5)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Home', True, WHITE)
        screen.blit(text_surface, text_surface.get_rect(center=home_button_center))

        pygame.display.flip()

        if not invaders:
            time.sleep(0.8)
            running = False


# ========================================================= #
#                     BRICK BREAKER                         #
# ========================================================= #
def brick_breaker(screen):
    paddle = pygame.Rect(SCREEN_WIDTH//2 - 75, SCREEN_HEIGHT - 60, 150, 18)
    ball = pygame.Rect(SCREEN_WIDTH//2 - 10, SCREEN_HEIGHT//2 - 10, 20, 20)
    ball_dx, ball_dy = 6, -6

    # create bricks
    bricks = []
    rows, cols = 5, 8
    brick_w = (SCREEN_WIDTH - 160) // cols
    brick_h = 24
    offset_x, offset_y = 80, 60
    for r in range(rows):
        for c in range(cols):
            bricks.append(pygame.Rect(offset_x + c * brick_w, offset_y + r * (brick_h + 6), brick_w - 6, brick_h))

    home_button_center = (100, SCREEN_HEIGHT - 100)
    home_button_radius = 50
    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = map_coords(*event.pos)
                if math.hypot(mx - home_button_center[0], my - home_button_center[1]) <= home_button_radius:
                    running = False
                else:
                    paddle.centerx = mx

        # mouse drag paddle
        if pygame.mouse.get_pressed()[0]:
            mx, my = map_coords(*pygame.mouse.get_pos())
            paddle.centerx = mx

        # move ball
        ball.x += ball_dx
        ball.y += ball_dy

        # wall collisions
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_dx = -ball_dx
        if ball.top <= 0:
            ball_dy = -ball_dy

        # paddle collision
        if ball.colliderect(paddle) and ball_dy > 0:
            ball.bottom = paddle.top
            ball_dy = -abs(ball_dy)
            hit_pos = (ball.centerx - paddle.left) / paddle.width
            ball_dx = int((hit_pos - 0.5) * 12)

        # brick collisions
        for brick in bricks[:]:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_dy = -ball_dy
                play_sound('./apps/app_3/brick_break.wav')
                break

        # bottom reset
        if ball.top > SCREEN_HEIGHT:
            ball.x = SCREEN_WIDTH//2 - ball.width//2
            ball.y = SCREEN_HEIGHT//2 - ball.height//2
            ball_dx, ball_dy = 6, -6
            time.sleep(0.5)

        # draw
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.ellipse(screen, BLUE, ball)
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)

        # home button
        pygame.draw.circle(screen, NAVY_BLUE, home_button_center, home_button_radius)
        pygame.draw.circle(screen, WHITE, home_button_center, home_button_radius, 5)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Home', True, WHITE)
        screen.blit(text_surface, text_surface.get_rect(center=home_button_center))

        pygame.display.flip()


# ========================================================= #
#                        MAIN MENU                          #
# ========================================================= #
def run(screen):
    running = True
    circle_radius = 100
    space_center = (SCREEN_WIDTH//3, SCREEN_HEIGHT//2)
    brick_center = (2*SCREEN_WIDTH//3, SCREEN_HEIGHT//2)
    home_center = (50 + circle_radius, SCREEN_HEIGHT - 50 - circle_radius)

    # load images
    try:
        space_img = pygame.image.load("./apps/app_3/space_invaders.jpg")
        space_img = pygame.transform.scale(space_img, (2*circle_radius, 2*circle_radius))
    except:
        space_img = None
    try:
        brick_img = pygame.image.load("./apps/app_3/brick_breaker.jpg")
        brick_img = pygame.transform.scale(brick_img, (2*circle_radius, 2*circle_radius))
    except:
        brick_img = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = map_coords(*event.pos)

                if math.hypot(x - space_center[0], y - space_center[1]) <= circle_radius:
                    play_sound('./apps/app_3/game_start.mp3')
                    space_invaders(screen)

                elif math.hypot(x - brick_center[0], y - brick_center[1]) <= circle_radius:
                    play_sound('./apps/app_3/game_start.mp3')
                    brick_breaker(screen)

                elif math.hypot(x - home_center[0], y - home_center[1]) <= circle_radius:
                    play_sound('./apps/app_3/back.wav')
                    running = False

        screen.fill(BLACK)

        # Space Invaders button
        if space_img:
            screen.blit(space_img, (space_center[0]-circle_radius, space_center[1]-circle_radius))
        pygame.draw.circle(screen, WHITE, space_center, circle_radius, 5)

        # Brick Breaker button
        if brick_img:
            screen.blit(brick_img, (brick_center[0]-circle_radius, brick_center[1]-circle_radius))
        pygame.draw.circle(screen, WHITE, brick_center, circle_radius, 5)

        # Home button
        pygame.draw.circle(screen, NAVY_BLUE, home_center, circle_radius)
        pygame.draw.circle(screen, WHITE, home_center, circle_radius, 5)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Home', True, WHITE)
        screen.blit(text_surface, text_surface.get_rect(center=home_center))

        pygame.display.flip()
        pygame.time.delay(50)


# ========================================================= #
#                     Standalone run                         #
# ========================================================= #
if __name__ == '__main__':
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Arcade')
    run(screen)
