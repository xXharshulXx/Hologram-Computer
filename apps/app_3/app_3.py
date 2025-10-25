import pygame
import sys
import os
import math
import time
from dotenv import load_dotenv

load_dotenv()
pygame.init()
mixer = pygame.mixer
mixer.init()

'''SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH',1920))
SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT',1080))
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)'''
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
    '''mapped_x = (y/1080) * 1920
    mapped_y = 1080 - ((x/1920) * 1080)'''
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
    run(screen)