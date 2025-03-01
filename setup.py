import pygame
import ctypes
import os

user32 = ctypes.windll.user32
dir_path = os.getcwd()

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)
SCALE_X = SCREEN_WIDTH/1280
SCALE_Y = SCREEN_HEIGHT/1080

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

#Font for images created

pygame.font.init()
font = pygame.font.SysFont(None, 100) #bigger font makes clearer text

#put r infront of strings to make them raw strings, path used for image loading

path = dir_path + r"\Images\ "
path = path.strip()

#Kuvat voi ladata tobytes/tostring vähentämään tilaa?

#BACKGROUNDS
path_background = path + r"background\ "
path_background = path_background.strip()

menu_background = pygame.image.load(path_background + "menu_background.jpg")
summer_forest = pygame.image.load(path_background + "summer_forest.jpg")

#BUTTONS
path_buttons = path + r"\buttons\ "
path_buttons = path_buttons.strip()

#MISC
path_misc = path + r"\misc\ "
path_misc = path_misc.strip()

menu_cursor = pygame.image.load(path_misc + "menu_cursor.png")

#Pictures created from text

new_game = font.render("NEW GAME", True, (0,0,0))
start = font.render("START", True, (0,0,0))
quit = font.render("QUIT", True, (0,0,0))
back = font.render("BACK", True, (0,0,0))
attack = font.render("ATTACK", True, (0,0,0))
special = font.render("SPECIAL", True, (0,0,0))
formation = font.render("FORMATION", True, (0,0,0))
