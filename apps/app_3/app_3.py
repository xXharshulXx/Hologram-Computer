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


SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH'))
SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT'))
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)


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
    mapped_x = (y/1080) * 1920
    mapped_y = 1080 - ((x/1920) * 1080)
    return int(mapped_x),int(mapped_y)


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

'''def brick_breaker(screen):'''
    # Continue with brick breaker 24/12/2025